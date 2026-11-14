# System Drop

Windows용 누적 낙하 해석 매니저. CalculiX / Abaqus 템플릿과 PyVista 결과 뷰어를 제공합니다.

## 다운로드

[v0.11.0 릴리스](https://github.com/younghuni0117-cloud/System_Drop/releases/tag/v0.11.0)에서 다음 파일을 받으세요.

- `system_drop_v0.11.0_windows_offline.zip`: Python 및 Windows x64 패키지를 포함한 오프라인 배포본 (약 363 MB).
- `system_drop_v0.11.0_windows.zip`: 일반 배포본 (약 29 MB). 필요한 환경이 없으면 인터넷 연결이 필요합니다.

오프라인용 ZIP 전체를 압축 해제하고 `start_windows.bat`을 실행하세요. 설치 안내는 압축 안의 `docs/OFFLINE_WINDOWS.md`를 참고하세요. 기존 실행 결과는 별도로 백업하여 보존하세요.

## 검증 범위

- 자동 테스트 170개 통과.
- Linux CalculiX 2.23에서 새 2재질 모델의 누적 낙하 2회 및 각 안정화 해석 완료.
- Windows 패키지 의존성 및 해시 검증 완료. 실제 Windows 오프라인 설치와 라이선스가 필요한 Abaqus 실행은 미검증입니다.
- 다양한 Abaqus 템플릿에 대한 검사·매핑을 제공하지만 모든 키워드 조합을 지원하는 것은 아닙니다. 지원 범위는 `docs/TEMPLATE_COMPATIBILITY.md`를 확인하세요.

배포본에 포함된 CalculiX 및 타사 구성요소의 라이선스·고지는 배포본 안의 관련 문서를 따릅니다.
