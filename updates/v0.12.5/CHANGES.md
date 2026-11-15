# v0.12.5 — Abaqus GUI 조건 반영과 Field/History 시간 출력

## 실제 실행 파일

생성한 drop_XX 폴더에서 **job.inp**가 실제 실행 입력입니다.
함께 복사한 abaqus_main.inp는 템플릿 사본이어서 조건이 다르게 보일 수 있습니다.
이제 README_INPUT.txt와 **input_settings.json**을 함께 생성해 실행 입력과 반영값을 명확히 표시합니다.
방향 셋업 단계에서 최종 job.inp를 다시 읽고 GUI와 대조하여 불일치가 있으면 완료 처리하지 않습니다.

## 반영 규칙

- GUI 종료 시간 → *DYNAMIC, EXPLICIT 자동 증분 데이터의 두 번째 필드.
- GUI 최대 증분 → 같은 데이터의 네 번째 필드.
- 양수인 GUI 최대 증분 → 해당 낙하 Step의 모든 Field 및 History 요청의 TIME INTERVAL.
- 최대 증분이 자동(0)이면 해석 상한을 비워두고 기존 출력 요청 간격은 유지합니다. TIME INTERVAL=0을 쓰지 않습니다.
- 기존 출력 변수와 NSET/ELSET, FILTER, VARIABLE, OP 등의 설정은 유지합니다.
- 상충하는 FREQUENCY, NUMBER INTERVAL, TIME POINTS, 기존 TIME INTERVAL만 정리합니다.
- Field/History 요청이 빠진 경우 기본 요청을 추가합니다.
- 최초 낙하와 다음 낙하 Import 입력 모두 출력 간격을 반영합니다.

예를 들어 종료 0.001초 / 최대 증분 0.00001초:

```text
*DYNAMIC, EXPLICIT
, 0.001, , 0.00001
...
*OUTPUT, FIELD, TIME INTERVAL=0.00001
...
*OUTPUT, HISTORY, TIME INTERVAL=0.00001
...
```

기존 자동 증분 데이터의 시간 스케일 계수(세 번째 필드)는 유지합니다.
DIRECT USER CONTROL / FIXED TIME INCREMENTATION은 GUI가 관리하는 자동 증분 상한 방식으로 전환합니다.
기존 고정 증분 모드를 유지해야 하는 모델은 이 Manager의 현재 관리 방식과 구분하여 검토해야 합니다.

## 회사 템플릿 대응

대소문자·주석·키워드 이어쓰기·기존 INCLUDE와 역할 매핑을 처리합니다.
키워드 순서와 고정 줄 번호에 의존하지 않고 대상 키워드를 찾아 수정합니다.
Marker 없는 템플릿에 Explicit Step이 여러 개이면 drop_step 매핑을 요구합니다.
선행 Step 이력을 임의 생략하거나, 모든 새로운 키워드 조합의 Import 적합성을 보장하지 않습니다.
기존 docs/TEMPLATE_COMPATIBILITY.md의 지원 범위와 사전 검사 제한은 유지합니다.

## 기본 템플릿과 업데이트

새 template_abaqus의 main/material/mesh 3개 파일을 업데이트 ZIP의 payload/template_abaqus에 포함합니다.
기본 main은 Field와 History 모두 TIME INTERVAL=0.000001을 사용합니다.
기존 두 재질 메쉬·물성·접촉·Section은 유지합니다.

업데이트 도구는 기존 3개 파일 모두 원래 기본 배포본 또는 새 템플릿과 해시가 일치할 때만
백업 후 기본 템플릿을 갱신합니다. **사용자가 수정한 템플릿은 덮어쓰지 않습니다.**
사용자 템플릿은 새 Manager의 키워드 처리 규칙으로 사용하면 됩니다.
새 기본 예제를 직접 사용할 경우 payload/template_abaqus를 별도 보관한 뒤 GUI 템플릿 경로로 선택할 수도 있습니다.

1. Manager와 결과창을 닫습니다. 진행 중이면 현재 단계 완료 후 일시정지합니다.
2. ZIP 전체를 새 임시 폴더에 풀고 apply_update.bat 실행.
3. 기존 start_windows.bat이 있는 프로그램 폴더 선택.
4. 다시 실행 → Abaqus 2025 → 새 실행의 최대 증분·종료 시간 설정 → 방향 셋업.
5. 생성한 drop_XX/job.inp 및 input_settings.json 확인.

기존 doe의 frozen template과 완료된 계산은 변경하지 않습니다.
기존 실행을 재개할 때는 그 실행의 저장 조건을 유지합니다. 조건을 바꾸려면 초기화 후 새 실행을 만드세요.
이전 패치를 모두 포함하고 라이브러리는 추가·재설치하지 않습니다.

## 검증과 공식 규칙

- 자동 테스트 203개 통과. GUI 값 readback, 자동 상한, 출력 요청 보존·충돌 제거,
  이어쓰기·주석·시간 스케일 계수·고정 모드 전환과 템플릿 원본 보존 포함.
- 실제 Qt GUI에서 Abaqus 미설치 상태로 최대 증분 0.00001 / 종료 0.001을 설정하고
  방향 셋업을 완료했습니다. 실행 파일 탐색 실패 전후에도 job.inp와 반영 보고서는 일치합니다.
- 실제 Abaqus 라이선스 실행과 Windows 업데이트 도구 실행은 이 환경에서 미검증입니다.

공식 2025 규칙:

- [DYNAMIC — Explicit 자동 증분 데이터](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEKEYRefMap/simakey-r-dynamic.htm)
- [OUTPUT — Field/History TIME INTERVAL와 배타적인 간격 옵션](https://docs.software.vt.edu/abaqusv2025/English/SIMACAEKEYRefMap/simakey-r-output.htm)
