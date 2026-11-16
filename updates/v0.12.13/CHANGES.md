# v0.12.13 — Pillow DLL 오류 진단과 반복 설치 안내 개선

## 이번 오류의 의미

`ImportError: DLL load failed while importing _imaging`은 Pillow의 이미지 처리 확장 모듈을 불러오지 못했다는 뜻입니다. Matplotlib이 Pillow를 호출하므로 rcsetup/colors/Image.py를 거쳐 나타날 수 있습니다. 해석을 시작하기 전 라이브러리 검사에서 발생한 오류입니다.

Windows용 Python/PySide6/VTK/Pillow 바이너리에는 Microsoft VC++ x64 런타임이 필요할 수 있습니다. 하지만 이미 설치했는데 같은 오류가 계속된다면 무조건 반복 설치할 이유는 없습니다. Pillow 파일 누락·혼합 버전·다른 DLL 의존성·실행 Python 불일치 등도 구분해야 합니다. 현재 PC에서 어떤 DLL이 실제로 실패하는지는 추가 진단 정보가 필요합니다.

## 변경 내용

- 모든 실패에 VC++ 설치를 권하던 공통 안내를 수정합니다. DLL 유형일 때만 V를 제공하고, 같은 프로그램 실행 중 VC++ 설치는 한 번만 안내합니다.
- VC++ 설치 결과를 성공 / 이미 설치됨 / 재부팅 필요 / 실패로 구분합니다. 3010/1641이면 Windows 재시작 안내 후 종료합니다. 1638/0x80070666이면 이미 설치된 경우로 안내합니다. 설치 로그는 logs/vc_runtime_install.log입니다.
- 성공적으로 설치한 Python 라이브러리를 재시도 때마다 다시 설치하지 않습니다.
- numpy → PIL.Image → PIL._imaging → matplotlib 등 모듈을 따로 검사합니다. 실패한 모듈, Python 경로·버전·비트 수, VC++ 설치 상태, Pillow 관련 DLL 검사 결과를 logs/runtime_import_check.txt 및 .json에 기록합니다.
- 검사와 실제 GUI에서 같은 PySide6 백엔드를 사용하고 다른 앱의 Qt 플러그인 환경변수를 제외합니다.
- MP4에만 사용하는 QtMultimedia 오류는 경고로 표시합니다. 필수 라이브러리가 정상이면 Manager·결과보기·AVI/GIF 사용은 계속 허용합니다. 필수 Pillow/QtWidgets/VTK 오류는 정상인 것처럼 건너뛰지 않습니다.

## Pillow 파일 검사·복구

Pillow 오류에서는 **P** 메뉴가 나타납니다.

1. Manager와 결과창을 닫고 새 업데이트를 적용합니다.
2. start_windows.bat으로 실행합니다.
3. `_imaging` 오류가 계속되면 **P**를 선택합니다.

동봉 Python 3.11의 Pillow 파일을 원본 Windows wheel과 비교합니다. **누락되거나 달라진 파일만** 백업 후 복구합니다. 동일한 파일과 다른 라이브러리, 시스템 Python은 변경하지 않습니다. 인터넷·pip 재설치는 사용하지 않습니다. 결과는 logs/pillow_repair.json, 변경 전 파일은 backups/pillow_repair_...에 보관합니다.

동봉 wheel의 해시가 다르거나 설치된 Pillow 버전이 동봉 버전과 다르면 자동으로 파일을 섞지 않고 중단합니다. pip가 설치 시 생성한 RECORD 메타데이터는 불필요하게 덮어쓰지 않습니다.

파일이 모두 정상이지만 DLL 오류가 계속될 수도 있습니다. 이 경우 P를 반복해도 달라지지 않습니다. **diagnose_windows.bat**으로 설치 없이 검사하고 logs/runtime_import_check.txt의 PIL_EXTENSION / DLL_PROBE 및 실패 메시지를 확인하세요. VC++ 설치 직후 아직 재부팅하지 않았다면 Windows를 한 번 재시작한 후 확인하세요.

## 적용 및 한계

apply_update.bat은 Manager가 시작되지 않는 상태에서도 실행할 수 있습니다. 추가 라이브러리 다운로드는 없으며 기존 offline 폴더의 Pillow wheel과 VC++ 설치 파일을 사용합니다. 기존 템플릿·runs·솔버를 보존합니다.

이 업데이트는 원인을 구분하고 Pillow의 파일 손상을 복구하는 기능을 제공합니다. 현재 사용자 PC의 누락 DLL을 직접 확인한 것은 아니므로 모든 _imaging 오류의 해결을 보장하지 않습니다.

## 검증

- 자동 테스트 **259개 통과**, 시작·복구 관련 30개 재확인.
- VC++ 반복 안내 제한, 재부팅 코드, 이미 설치됨 코드, 패키지 재설치 생략, Qt 환경 정리, 선택적 MP4 오류 구분을 확인했습니다.
- 실제 동봉 Windows Pillow wheel에서 확장 모듈을 복구하고 원본 해시 일치 및 두 번째 검사에서 파일을 다시 쓰지 않는 것을 검증했습니다. 이는 Linux에서 파일 복구 경로를 검증한 것으로 Windows DLL 로드 성공 검증은 아닙니다.
- Linux 실제 라이브러리 검사에서도 Pillow/Image/_imaging/Matplotlib/Qt/VTK/PyVista를 모두 불러오는 것을 확인했습니다. 사용자 Windows의 실제 실패 DLL은 새 진단 로그로 확인해야 합니다.
