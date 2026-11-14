"""Reuse Python environments; invoke pip only for missing/incompatible requirements.

No exe creation, no forced reinstall, no automatic venv recreation.
This module uses only the Python standard library until the GUI is launched.
"""
from __future__ import print_function

import argparse
import importlib.util
import importlib.metadata
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT=Path(__file__).resolve().parent
# Embeddable CPython runs in isolated mode: neither the working directory nor
# the script directory is guaranteed to be on sys.path. Resolve local helpers
# explicitly before importing them, including when this script was relocated.
sys.path.insert(0,str(ROOT))


def configure_portable_paths(root=ROOT):
    """Repair only our embedded runtime; never touch a system/venv Python."""
    root=Path(root).resolve()
    target=root/'runtime/python311'
    if Path(sys.executable).parent.resolve()!=target.resolve():return
    # Child processes using -c also need installed wheels. Repair an absent
    # or stale _pth before running their import checks.
    content='python311.zip\n.\nLib\nLib/site-packages\n../..\nimport site\n'
    path_file=target/'python311._pth'
    if not path_file.is_file() or path_file.read_text(encoding='utf-8-sig')!=content:
        path_file.write_text(content,encoding='utf-8')
    for path in (target/'Lib',target/'Lib/site-packages'):
        if path.is_dir() and str(path) not in sys.path:sys.path.append(str(path))


REQUIREMENTS=[
    ("numpy","numpy",(1,24)),
    ("PySide6","PySide6.QtWidgets",(6,8,2)),
    ("pyvista","pyvista",(0,44)),
    ("pyvistaqt","pyvistaqt",(0,11)),
    ("Pillow","PIL",(9,0)),
    ("matplotlib","matplotlib",(3,5)),
]


def missing_requirements():
    missing=[]
    for distribution,module,minimum in REQUIREMENTS:
        requirement=distribution+">="+".".join(map(str,minimum))
        try:
            present=importlib.util.find_spec(module) is not None
            try: version=importlib.metadata.version(distribution)
            except importlib.metadata.PackageNotFoundError:
                if distribution=="PySide6": version=importlib.metadata.version("PySide6-Essentials")
                else: raise
            numbers=tuple(int(n) for n in re.findall(r"\d+",version)[:len(minimum)])
            if not present or numbers<minimum: missing.append(requirement)
        except (ModuleNotFoundError,ImportError,OSError,RuntimeError,ValueError,importlib.metadata.PackageNotFoundError):
            missing.append(requirement)
    # These are transitive runtime dependencies; do not reinstall parent packages.
    for module,distribution in (("vtk","vtk"),("qtpy","QtPy")):
        if importlib.util.find_spec(module) is None: missing.append(distribution)
    # The portable environment has a fixed, complete wheel closure. Check
    # missing transitive distributions too, so an interrupted install can retry.
    portable=ROOT/'runtime/python311'
    if Path(sys.executable).parent.resolve()==portable.resolve() and (ROOT/'offline/manifest.json').exists():
        pins=json.loads((ROOT/'offline/manifest.json').read_text(encoding='utf-8'))['pins']
        for name in pins:
            if name.lower()=='pip':continue
            try:importlib.metadata.version(name)
            except importlib.metadata.PackageNotFoundError:
                if not any(r.split('>=')[0].lower().replace('-','_')==name.lower().replace('-','_') for r in missing):missing.append(name)
    return missing


def candidate_interpreters(root=ROOT):
    paths=[Path(sys.executable),root/"runtime/python311/python.exe"]
    if os.environ.get("SYSTEM_DROP_PYTHON"): paths.insert(0,Path(os.environ["SYSTEM_DROP_PYTHON"]))
    relative=Path("Scripts/python.exe") if os.name=="nt" else Path("bin/python")
    paths.append(Path(sys.base_prefix)/("python.exe" if os.name=="nt" else "bin/python"))
    for base in (root,root.parent,root.parent.parent):
        paths.append(base/".venv"/relative)
    if os.environ.get("VIRTUAL_ENV"): paths.append(Path(os.environ["VIRTUAL_ENV"])/relative)
    cache=root/".python_path"
    if cache.is_file():
        try: paths.append(Path(cache.read_text(encoding="utf-8").strip()))
        except OSError: pass
    # Reuse v0.1's environment when a new zip is extracted next to the old version.
    try:
        siblings=list(root.parent.parent.glob("system_drop*"))[:40]
        for sibling in siblings:
            paths.extend((sibling/".venv"/relative,sibling/"system_drop/.venv"/relative))
    except OSError: pass
    seen=set()
    for path in paths:
        # A venv Python is often a symlink on Linux. Resolving it selects the base
        # interpreter and loses the venv's installed packages.
        key=os.path.normcase(str(path.absolute()))
        if key not in seen and path.is_file():
            seen.add(key); yield path.absolute()


def select_interpreter(root=ROOT,probe=None):
    def run_probe(path):
        if path==Path(sys.executable).absolute(): return missing_requirements()
        result=subprocess.run([str(path),str(ROOT/"bootstrap_windows.py"),"--probe"],
                              capture_output=True,text=True,encoding="utf-8",timeout=20)
        if result.returncode: raise RuntimeError("Python environment unavailable")
        return json.loads(result.stdout.strip().splitlines()[-1])["missing"]
    probe=probe or run_probe
    best=None
    for path in candidate_interpreters(root):
        try: missing=probe(path)
        except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired): continue
        if best is None or len(missing)<len(best[1]): best=(path,missing)
        if not missing: return path,missing
    if best is None: raise RuntimeError("Python 3.10 이상 실행 환경을 찾지 못했습니다.")
    return best


def ensure_requirements(interpreter,missing,run=subprocess.run):
    if not missing:
        print("Dependencies already available; starting without pip.",flush=True)
        return 0
    print("Installing only missing/incompatible packages: "+", ".join(missing),flush=True)
    return run([str(interpreter),"-m","pip","install",*missing],cwd=str(ROOT)).returncode


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--probe",action="store_true")
    parser.add_argument("--install-only",action="store_true")
    parser.add_argument("--launch",action="store_true")
    parser.add_argument("--offline",action="store_true")
    parser.add_argument("--gui",action="store_true",help=argparse.SUPPRESS)
    args=parser.parse_args()
    if sys.version_info<(3,10):
        print("Python 3.10 or newer is required."); return 1
    configure_portable_paths()
    if args.gui:
        import runpy
        runpy.run_module('system_drop.gui',run_name='__main__')
        return 0
    if args.probe:
        print(json.dumps({"missing":missing_requirements()}));return 0
    interpreter,missing=select_interpreter()
    print("[1/4] Python: "+str(interpreter),flush=True)
    offline=args.offline or (ROOT/'offline/manifest.json').is_file()
    if offline:
        from offline_setup import guide,prepare_python,runtime_check
        if not missing:
            check=runtime_check(interpreter,ROOT)
            if check.returncode:
                print('기존 환경을 실제로 불러오지 못해 동봉 전용 환경으로 전환합니다.',flush=True)
                missing=['portable_fallback']
        if missing:
            interpreter=prepare_python(ROOT)
            probe=subprocess.run([str(interpreter),str(ROOT/'bootstrap_windows.py'),'--probe'],capture_output=True,text=True,encoding='utf-8')
            if probe.returncode:raise RuntimeError('동봉 Python 실행 실패. VC++ 런타임/Windows x64 환경을 확인하세요.\n'+probe.stderr)
            missing=json.loads(probe.stdout.strip().splitlines()[-1])['missing']
        code=guide(ROOT,interpreter,missing)
    else:code=ensure_requirements(interpreter,missing)
    if code: return code
    try: (ROOT/".python_path").write_text(str(interpreter),encoding="utf-8")
    except OSError: pass
    if args.install_only:
        print("Ready. Run start_windows.bat.");return 0
    env=os.environ.copy();env['QT_API']='pyside6'
    env.pop('QT_PLUGIN_PATH',None);env.pop('QT_QPA_PLATFORM_PLUGIN_PATH',None)
    if os.name=='nt':env['QT_QPA_PLATFORM']='windows'
    # Enter the GUI through this file so the child also initializes sys.path.
    return subprocess.call([str(interpreter),str(ROOT/'bootstrap_windows.py'),"--gui"],cwd=str(ROOT),env=env)


if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as exc:
        print("Startup failed: "+str(exc),flush=True)
        try:
            import traceback
            (ROOT/'logs').mkdir(exist_ok=True)
            report=ROOT/'logs/startup_error.txt'
            report.write_text('Python: '+sys.executable+'\nRoot: '+str(ROOT)+'\nsys.path: '+repr(sys.path)+'\n\n'+traceback.format_exc(),encoding='utf-8')
            print('Details: '+str(report),flush=True)
        except OSError:pass
        raise SystemExit(1)
