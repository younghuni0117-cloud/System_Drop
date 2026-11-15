# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.10 업데이트 — CalculiX main/material/mesh 3파일 직접 실행

**[v0.12.10 누적 업데이트 ZIP 다운로드 · 약 260 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.10_update.zip)**

새 CalculiX 실행은 **calculix_main.inp / calculix_material.inp / calculix_mesh.inp** 세 파일만 생성합니다.
**job.inp 진입 파일을 생성하지 않습니다.** Manager의 최대 증분과 종료 시간은 생성된 **calculix_main.inp**에 반영합니다.
실제 명령은 **ccx -i calculix_main**이며 결과와 재시작도 calculix_main.frd/dat/rin/rout을 사용합니다.
진행률·변환·누적 상태 연결·완료 결과 재사용도 새 이름을 따릅니다.

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP 전체를 임시 폴더에 풀고 apply_update.bat을 실행합니다.
3. 기존 start_windows.bat이 있는 설치 폴더를 선택합니다.
4. 새 실행의 3개 INP, main의 DYNAMIC 시간 행 및 input_settings.json을 확인합니다.

이전 완료 job 형식은 소급 변경하지 않고 보존합니다. 이전 완료 결과에서 다음 낙하를 새 형식으로 연결할 수 있습니다.
누적 단계의 material/mesh include는 재정의를 하지 않는 주석 파일이며 실제 변형·재료 이력은 native rin으로 계승합니다.
Abaqus 3파일 구조, 이전 출력량 개선도 유지합니다. 추가 패키지는 없습니다.
자동 테스트 **225개 통과**, Linux CalculiX 2.23 짧은 2방향 직접 실행과 이전 job 상태에서 새 main으로 연결하는 실제 테스트를 모두 완료했습니다.
[파일 구조·시간 반영·기존 실행 호환·검증](updates/v0.12.10/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.10 업데이트** 적용 → start_windows.bat 실행.
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
