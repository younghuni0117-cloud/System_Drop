# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.8 업데이트 — CalculiX 결과 파일 용량·변환 시간 개선

**[v0.12.8 누적 업데이트 ZIP 다운로드 · 약 244 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.8_update.zip)**

매 계산 증분마다 FRD/DAT를 기록하던 설정을 자동 기록 주기로 바꿉니다.
상세 옵션에 **CalculiX 기록 주기(증분)**와 **최대 저장 Frame(기본 1,000)**을 추가했습니다.
최대 저장 수는 단계별 변환 한도이며 원본 파일 크기의 강제 상한은 아닙니다. 실제 기록 간격은 자동 계산 증분에 따라 달라집니다.
짧은 응력 피크를 평가하려면 기록 주기를 작게 설정하세요.
DAT 검사 중 전체 프레임의 평균/최대 응력을 미리 계산하던 작업도 줄였습니다. 수치 검증은 유지합니다.

짧은 실제 Linux CalculiX 2.23 충돌 비교에서 FRD+DAT는 **70.4MB → 7.5MB(약 89% 감소)**,
변환은 **5.48초 → 0.86초**였습니다. 두 해석의 최종 native 변형·속도·응력·소성 상태가 완전히 동일했습니다.
이는 짧은 테스트 측정이며 Windows의 전체 실행 시간이나 20~40GB 사례에 대한 보장 수치는 아닙니다.

1. 현재 단계 완료 후 일시정지하고 Manager와 결과창을 닫습니다.
2. ZIP 전체를 임시 폴더에 풀고 apply_update.bat을 실행합니다.
3. 기존 start_windows.bat이 있는 설치 폴더를 선택합니다.
4. 재실행 후 상세 옵션의 새 기록 설정을 확인합니다. 기본은 자동 / 최대 1,000프레임입니다.

이전 업데이트를 모두 포함합니다. 기존 runs·템플릿·라이브러리·솔버를 보존하며 추가 패키지는 없습니다.
기존 대용량 완료 결과는 재개로 솔버 재계산 없이 개선된 변환을 재시도할 수 있습니다. 원본은 자동 삭제하거나 축소하지 않습니다.
자동 테스트 **214개 통과**, 짧은 2방향 누적 해석도 완료했습니다.
[변경 내용·설정·검증](updates/v0.12.8/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.8 업데이트** 적용 → start_windows.bat 실행.
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
