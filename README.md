# System Drop

Windows용 누적 낙하 해석 Manager. CalculiX / Abaqus 입력과 PyVista 결과창을 제공합니다.
배포는 **기본 오프라인 설치본 + 작은 누적 업데이트** 방식입니다.

## 최신 v0.12.12 업데이트 — 템플릿 제품 집합 정의 유지

**[v0.12.12 누적 업데이트 ZIP 다운로드 · 약 267 KB](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_v0.12.12_update.zip)**

CalculiX/Abaqus 모두 **템플릿 mesh의 PRODUCT_NODES / PRODUCT_ELEMENTS**를 사용합니다.
AUTO_PRODUCT_* 집합을 추가하지 않으며 기존 제품 집합을 자동 확장·재생성하지 않습니다.
GENERATE와 하위 집합 참조 등 기존 정의를 유지합니다. 집합이 없거나 범위가 제품 전체와 다르면 원본 템플릿을 확인하도록 안내합니다.
마커 없는 Abaqus와 Assembly의 기존 제품 집합도 대응시켜 사용합니다.

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP 전체를 임시 폴더에 풀고 apply_update.bat으로 기존 설치를 선택합니다.
3. 새 실행에서 main의 PRODUCT_* 참조 및 첫 낙하 mesh의 기존 집합 정의를 확인합니다.

main/material/mesh 3개 INP, GUI 시간 설정, drop_01_drop.frd 등의 결과명은 유지합니다.
기존 완료 입력과 native 상태를 소급 변경하지 않습니다. 템플릿·runs·라이브러리·솔버를 보존하며 추가 패키지는 없습니다.
자동 테스트 **244개 통과**. Linux CalculiX 2.23 짧은 2방향 누적 해석에서 AUTO_PRODUCT_* 미생성과 템플릿 집합 계승을 확인했습니다.
첫 낙하의 최종 변형·속도·응력·소성 상태도 이전 AUTO 집합 방식과 완전히 동일했습니다.
Windows 및 Abaqus 라이선스 실행은 이번 실제 검증에 포함하지 않았습니다.
[템플릿 보존 범위·집합 오류 안내·검증](updates/v0.12.12/CHANGES.md).

## 최초 오프라인 설치 — 기본 v0.11.0

GitHub 단일 파일 제한에 맞춘 363MB 원본 ZIP의 분할 파일입니다.
아래 **분할 5개 + join_files.bat**을 모두 같은 폴더에 원래 파일명으로 저장하세요.

- [분할 1 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part001)
- [분할 2 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part002)
- [분할 3 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part003)
- [분할 4 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part004)
- [분할 5 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/system_drop_offline.zip.part005)
- [join_files.bat 다운로드](https://github.com/younghuni0117-cloud/System_Drop/raw/refs/heads/main/downloads/join_files.bat)

join_files.bat 실행 → 생성된 ZIP 전체 압축 해제 → 위 **최신 v0.12.12 업데이트** 적용 → start_windows.bat 실행.
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
