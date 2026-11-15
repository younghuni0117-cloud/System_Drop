# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.9 업데이트 — CalculiX 실제 main 입력과 시간 설정 검증

**[v0.12.9 누적 업데이트 ZIP 다운로드 · 약 254 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.9_update.zip)**

CalculiX에서 실제로 실행한 job.inp와 같은 폴더의 수정 전 calculix_main.inp 사본이 혼동되는 문제를 정리했습니다.
새 실행은 **job.inp → calculix_main.inp**로 INCLUDE합니다. 실제 모델·시간 조건을 main에서 확인할 수 있고 job.frd/dat/rin/rout 이름은 유지합니다.
job.inp는 필요한 진입 파일이므로 함께 유지하세요. Abaqus는 기존 3파일 구조를 유지합니다.

INCLUDE를 펼친 최종 입력을 생성 후와 솔버 시작 직전에 GUI/실행 설정과 대조합니다.
각 단계의 **input_settings.json / README_INPUT.txt**에 반영값과 실제 입력 경로를 기록합니다.
CalculiX EXPLICIT=2와 Abaqus EXPLICIT의 서로 다른 시간 필드 및 전용 옵션 혼용을 검사합니다.
최대 증분·실제 계산 증분·결과 프레임 기록 간격은 서로 다릅니다.

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP 전체를 임시 폴더에 풀고 apply_update.bat을 실행합니다.
3. 기존 start_windows.bat이 있는 설치 폴더를 선택합니다.
4. 새 실행의 calculix_main.inp와 input_settings.json을 확인합니다.

이전 업데이트와 v0.12.8 출력량 개선을 모두 포함합니다. 기존 runs·템플릿·라이브러리·솔버를 보존하며 추가 패키지는 없습니다.
완료된 기존 입력은 해시를 보존하므로 소급 변경하지 않습니다. 이전 버전 완료 실행은 당시의 실제 job.inp를 확인하세요.
자동 테스트 **220개 통과**, Linux CalculiX 2.23 짧은 2방향 낙하+안정화도 모두 완료했습니다.
실제 Windows 및 Abaqus 라이선스 실행은 이번 검증에 포함하지 않았습니다.
[파일 역할·두 솔버의 시간 데이터 형식·검증](updates/v0.12.9/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.9 업데이트** 적용 → start_windows.bat 실행.
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
