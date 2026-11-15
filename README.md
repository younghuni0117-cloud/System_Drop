# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.5 업데이트 — Abaqus GUI 조건과 출력 간격

**[v0.12.5 누적 업데이트 ZIP 다운로드 · 약 233 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.5_update.zip)**

GUI의 종료 시간·최대 증분을 실제 **job.inp**에 반영하고 Field·History의 TIME INTERVAL을 함께 갱신합니다. 기존 출력 변수·영역과 추가 옵션은 유지합니다. **input_settings.json**으로 실제 입력을 다시 읽어 GUI와 대조합니다. abaqus_main.inp는 템플릿 사본이며 실제 실행 파일은 job.inp입니다.

1. Manager와 결과창을 닫습니다. 계산 중이면 현재 단계 완료 후 일시정지합니다.
2. ZIP 전체를 새 임시 폴더에 풀고 **apply_update.bat** 실행.
3. 기존 **start_windows.bat**이 있는 프로그램 폴더 선택.
4. 다시 실행 → Abaqus 2025 → GUI 시간 설정 → 방향 셋업 → job.inp와 input_settings.json 확인.

원래 기본 Abaqus 템플릿으로 식별되면 3개 INP를 백업 후 갱신합니다. **사용자가 수정한 템플릿은 덮어쓰지 않습니다.** 새 기본 템플릿은 ZIP의 payload/template_abaqus에도 있습니다.

이전 패치를 모두 포함하고 기존 runs·설정·라이브러리·솔버를 보존합니다. 조건을 바꾸려면 새 실행을 만드세요.
자동 테스트 **203개 통과**, 실제 Qt GUI에서 Abaqus 미설치 상태의 설정·입력 생성과 실행 파일 부재 전후 입력 보존을 확인했습니다. 실제 Abaqus 및 Windows 업데이트 도구 실행은 미검증입니다.

[변경 내용·템플릿 처리·공식 규칙](updates/v0.12.5/CHANGES.md) · [GUI 설정 검증](updates/v0.12.5/abaqus0125_ui_summary.json)

기존 MemoryError 복구는 이전과 같이 **이전 실행 폴더 열기 / 재개**로 원본 FRD/DAT/native/완료 기록을 확인한 뒤 솔버 재계산 없이 변환을 재시도합니다. [복구 안내](updates/v0.12.4/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.5 업데이트** 적용 → start_windows.bat 실행.
Windows 10/11 x64용 Python과 로컬 설치 패키지를 포함합니다. 오프라인 환경에서는 기본 설치본을 매번 다시 받을 필요가 없습니다.

원본 오프라인 ZIP SHA-256:
`38077357d358853468fc020d3099217bf401091bc1eb83d433bc9edb33184398`

## 검증과 이전 변경 기록

실제 FEM 계산은 Linux CalculiX 2.23에서 시험했습니다. 실제 Windows 실행과 라이선스가 필요한 Abaqus 실행은 이 개발 환경에서 미검증입니다.
임의 Abaqus 키워드 조합의 지원 범위는 배포본의 docs/TEMPLATE_COMPATIBILITY.md를 확인하세요.

- [v0.12.4 결과 변환 메모리](updates/v0.12.4/CHANGES.md)
- [v0.12.3 Windows 실행 환경·충돌 진단](updates/v0.12.3/CHANGES.md)
- [v0.12.2 결과창 실행 경로](updates/v0.12.2/CHANGES.md)
- [v0.12.1 GUI 시작 인수](updates/v0.12.1/CHANGES.md)
- [v0.12.0 결과창·방향 모식도](updates/v0.12.0/CHANGES.md)

배포본의 CalculiX 및 타사 구성요소는 각 라이선스·고지를 따릅니다.
