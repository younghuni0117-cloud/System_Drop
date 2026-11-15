# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.6 업데이트 — Abaqus 3파일 구조와 프로그램 위치 기준 runs

**[v0.12.6 누적 업데이트 ZIP 다운로드 · 약 238 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.6_update.zip)**

새 Abaqus 실행은 **abaqus_main.inp / abaqus_material.inp / abaqus_mesh.inp**로 나누어 main에서 INCLUDE합니다.
실제 솔버 input도 abaqus_main.inp를 사용합니다. 중복 job.inp를 생성 폴더에 남기지 않습니다.
GUI 시간·증분과 Field/History 설정 검증은 그대로 유지합니다.

상세 옵션의 새 결과 위치는 **현재 프로그램 폴더/runs**로 고정합니다. 다른 PC의 저장된 절대 경로를 불러와도 현재 프로그램을 기준으로 적용합니다.
기존 실행을 재개할 때는 선택한 기존 폴더에서 이어갑니다.

1. Manager와 결과창을 닫습니다. 실행 중이면 현재 단계 완료 후 일시정지합니다.
2. ZIP 전체를 새 임시 폴더에 풀고 apply_update.bat 실행.
3. 기존 start_windows.bat이 있는 설치 폴더 선택.
4. 프로그램 재실행 후 새 실행에서 파일 구조·상세 옵션 경로 확인.

이전 패치를 모두 포함합니다. 기존 실행의 job.inp는 계속 지원하고 사용자 템플릿·runs·설정·라이브러리·솔버를 보존합니다.
자동 테스트 **207개 통과**. 실제 Abaqus 및 Windows 업데이트 실행은 미검증입니다.
[변경 내용·Import 파일 역할·검증](updates/v0.12.6/CHANGES.md).

기존 MemoryError는 **이전 실행 폴더 열기 / 재개**로 원본 완료 상태를 확인한 뒤 솔버 재계산 없이 변환부터 재시도합니다. [복구 안내](updates/v0.12.4/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.6 업데이트** 적용 → start_windows.bat 실행.
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
