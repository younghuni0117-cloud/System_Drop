# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.13 업데이트 — Pillow DLL 오류 진단·반복 설치 안내 개선

**[v0.12.13 누적 업데이트 ZIP 다운로드 · 약 275 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.13_update.zip)**

VC++ 설치 후 같은 안내가 반복되는 시작 흐름을 보완했습니다.
_imaging 오류는 Pillow의 이미지 처리 DLL 로드 문제입니다. VC++를 이미 설치했다면 반복 설치보다 Pillow 파일과 DLL 의존성 확인이 필요합니다.
설치 완료 / 이미 설치됨 / Windows 재시작 필요 / 실패를 구분하고, 같은 실행에서 V 설치를 반복 안내하지 않습니다.

1. Manager·결과창을 닫고 ZIP의 apply_update.bat으로 기존 설치에 적용합니다. Manager가 시작되지 않아도 업데이트할 수 있습니다.
2. start_windows.bat으로 실행합니다. _imaging 오류가 계속되면 **P**로 동봉 Pillow 파일을 검사·복구합니다.
3. 같은 파일은 다시 쓰지 않고 다른 라이브러리·시스템 Python은 변경하지 않습니다. 인터넷이나 pip 재설치는 사용하지 않습니다.
4. 여전히 실패하면 **diagnose_windows.bat**으로 설치 없이 검사하고 logs/runtime_import_check.txt를 확인합니다.

VC++ 설치 후 아직 Windows를 재시작하지 않았다면 한 번 재시작한 후 확인하세요.
동봉 원본이 손상됐거나 Pillow 버전이 다르면 자동으로 파일을 섞지 않습니다. 원본이 정상이어도 다른 DLL 의존성 문제는 남을 수 있어 Windows의 실제 오류 로그 확인이 필요합니다.
기존 해석 기능·템플릿·runs·솔버는 유지합니다. 새 라이브러리 다운로드는 없습니다.
자동 테스트 **259개 통과**. 실제 동봉 Windows Pillow wheel의 파일 복구·해시와 반복 검사 시 재작성 생략을 검증했습니다. 사용자 Windows의 DLL 로드 성공은 아직 미검증입니다.
[필요한 런타임·Pillow 복구·진단 로그·검증](updates/v0.12.13/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.13 업데이트** 적용 → start_windows.bat 실행.
Windows 10/11 x64용 Python과 로컬 설치 패키지를 포함합니다. 오프라인 환경에서는 기본 설치본을 매번 다시 받을 필요가 없습니다.

원본 오프라인 ZIP SHA-256:
`38077357d358853468fc020d3099217bf401091bc1eb83d433bc9edb33184398`

## 검증과 이전 변경 기록

실제 FEM 계산은 Linux CalculiX 2.23에서 시험했습니다. 실제 Windows 실행과 라이선스가 필요한 Abaqus 실행은 이 개발 환경에서 미검증입니다.
임의 Abaqus 키워드 조합의 지원 범위는 배포본의 docs/TEMPLATE_COMPATIBILITY.md를 확인하세요.

- [v0.12.5 Abaqus GUI 조건 반영](updates/v0.12.5/CHANGES.md)
- [v0.12.4 결과 변환 메모리](updates/v0.12.4/CHANGES.md)
- [v0.12.3 Windows 실행 환경·충돌 진단](updates/v0.12.3/CHANGES.md)
- [v0.12.2 결과창 실행 경로](updates/v0.12.2/CHANGES.md)
- [v0.12.1 GUI 시작 인수](updates/v0.12.1/CHANGES.md)
- [v0.12.0 결과창·방향 모식도](updates/v0.12.0/CHANGES.md)

배포본의 CalculiX 및 타사 구성요소는 각 라이선스·고지를 따릅니다.
