"""Offline Windows x64 setup guide. Standard library only, no network fallback."""
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile


def manifest(root):return json.loads((Path(root)/'offline/manifest.json').read_text(encoding='utf-8'))


def verify(root):
    root=Path(root);data=manifest(root)
    for name,expected in data['files'].items():
        path=root/'offline'/name
        if not path.is_file():raise RuntimeError('오프라인 파일 누락: '+name)
        h=hashlib.sha256()
        with path.open('rb') as stream:
            for part in iter(lambda:stream.read(1024*1024),b''):h.update(part)
        if h.hexdigest()!=expected:raise RuntimeError('오프라인 파일 손상: '+name+' (압축파일을 다시 복사/해제하세요.)')
    return data


def prepare_python(root):
    root=Path(root);target=root/'runtime/python311';exe=target/'python.exe'
    if not exe.exists():
        data=manifest(root);archive=root/'offline'/data['python_archive']
        if hashlib.sha256(archive.read_bytes()).hexdigest()!=data['files'][data['python_archive']]:raise RuntimeError('동봉 Python 압축파일 해시가 다릅니다.')
        target.mkdir(parents=True,exist_ok=True)
        with zipfile.ZipFile(archive) as z:
            for entry in z.namelist():
                if not (target/entry).resolve().is_relative_to(target.resolve()):raise RuntimeError('잘못된 Python 압축 경로')
            z.extractall(target)
    (target/'Lib/site-packages').mkdir(parents=True,exist_ok=True)
    (target/'python311._pth').write_text('python311.zip\n.\nLib\nLib/site-packages\n../..\nimport site\n',encoding='utf-8')
    return exe


def install(root,interpreter,missing,run=subprocess.run):
    root=Path(root);data=verify(root);pins=data['pins']
    names=[r.split('>=')[0].lower().replace('-','_') for r in missing]
    requirements=[name+'=='+version for name,version in pins.items() if name.lower().replace('-','_') in names]
    known={r.split('==')[0].lower().replace('-','_') for r in requirements}
    if any(name not in known for name in names):raise RuntimeError('동봉 패키지 목록에 없는 항목: '+', '.join(names))
    print('[3/4] 동봉 wheel에서 필요한 항목만 설치합니다. 인터넷에 접속하지 않습니다.',flush=True)
    return run([str(interpreter),str(root/'tools/install_local_wheels.py'),*requirements],cwd=str(root)).returncode


def runtime_check(interpreter,root):
    code="import numpy,matplotlib,qtpy,PySide6.QtWidgets,PySide6.QtMultimedia,vtk,pyvista,pyvistaqt,PIL; assert hasattr(PySide6.QtMultimedia,'QVideoFrameInput'); print('IMPORT_OK')"
    return subprocess.run([str(interpreter),'-c',code],cwd=str(root),capture_output=True,text=True,encoding='utf-8',errors='replace')


def guide(root,interpreter,missing):
    root=Path(root);(root/'logs').mkdir(exist_ok=True)
    while True:
        try:
            print('[2/4] 오프라인 환경과 필요한 패키지 확인',flush=True)
            if not missing:print('[3/4] 라이브러리가 이미 있어 설치를 생략합니다.',flush=True)
            code=install(root,interpreter,missing) if missing else 0
            if code:raise RuntimeError('로컬 패키지 설치 실패 (종료 코드 '+str(code)+')')
            print('[4/4] 실제 라이브러리 불러오기 검사',flush=True)
            check=runtime_check(interpreter,root)
            if check.returncode:raise RuntimeError(check.stdout+'\n'+check.stderr)
            print('준비 완료. Manager를 실행합니다.',flush=True);return 0
        except Exception as exc:
            message=str(exc);(root/'logs/offline_setup_error.txt').write_text(message,encoding='utf-8')
            print('\n오프라인 준비를 완료하지 못했습니다:\n'+message,flush=True)
            print('설치 파일 전체를 복사했는지 확인하세요. DLL 오류라면 V로 동봉 VC++ 런타임을 설치하세요.',flush=True)
            if not sys.stdin.isatty():return 1
            answer=input('[R] 다시 시도 / [V] VC++ 런타임 설치 / [Q] 종료: ').strip().lower()
            if answer=='q':return 1
            if answer=='v':subprocess.run(['powershell','-NoProfile','-ExecutionPolicy','Bypass','-File',str(root/'tools/install_vc_runtime.ps1')])
