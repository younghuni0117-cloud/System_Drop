# v0.12.9 — CalculiX 실제 입력 파일과 시간 설정 검증

## 확인된 원인

CalculiX는 `ccx -i job`으로 `job.inp`를 실행했습니다. GUI 값은 이 파일에 기록했지만, 같은 실행 폴더의 `calculix_main.inp`는 수정 전 템플릿 사본으로 남았습니다. 따라서 main 파일만 열면 설정이 반영되지 않은 것처럼 보였습니다.

결과창은 결과 파일의 실제 프레임 시간과 누적 시간을 표시합니다. 그 화면이 정상이라는 이유만으로 입력의 최대 증분·종료 시간 반영 여부를 판단할 수는 없습니다.

## 변경 내용

- 새 CalculiX 실행에서 실제 모델·해석 조건은 **calculix_main.inp**에 둡니다.
- **job.inp**는 `*INCLUDE, INPUT=calculix_main.inp`로 연결하는 작은 진입 파일입니다. `ccx -i job` 명령과 `job.frd / job.dat / job.rin / job.rout` 파일 이름을 유지합니다. job.inp도 함께 보존해야 합니다.
- 첫 낙하 main은 material / mesh INCLUDE와 함께 실제 조건을 포함합니다. 누적 단계의 main은 native `*RESTART, READ`와 새 절차 조건을 포함합니다. 재시작 단계에서 메쉬·재료를 다시 정의하지 않습니다.
- 첫 낙하·안정화·다음 낙하 생성 후, 그리고 솔버 시작 직전에 INCLUDE를 펼친 실제 입력을 읽어 GUI/실행 설정과 대조합니다. 종료 시간·초기/최소/최대 증분·Explicit/Implicit 구분·결과 기록 주기를 검증합니다.
- 각 단계에 **input_settings.json** 및 **README_INPUT.txt**를 생성합니다. actual_input, model_input, expected, actual, errors로 실행 입력과 반영값을 확인할 수 있습니다.
- 아직 계산하지 않은 기존 준비 단계는 실행 전 새 구조로 정리합니다. 완료 결과의 재변환은 기존 입력·완료 기록을 보존하며 솔버를 다시 실행하지 않습니다.
- Abaqus는 기존 **abaqus_main/material/mesh** 구조와 실행 방식을 유지합니다. `EXPLICIT=2`를 Abaqus에 사용하는 경우, 또는 Abaqus 전용 시간 옵션을 CalculiX에 사용하는 경우를 검사합니다. 임의의 모든 솔버 키워드를 검증하는 완전한 datacheck는 아닙니다.

## 두 솔버의 시간 데이터 행은 다릅니다

| 절차 | 키워드 | 1열 | 2열 | 3열 | 4열 |
|---|---|---|---|---|---|
| CalculiX 낙하 | `*DYNAMIC, EXPLICIT=2` | 초기 증분 기준값 | 단계 종료 시간 | 최소 증분 | 최대 증분 |
| Abaqus 자동 Explicit 낙하 | `*DYNAMIC, EXPLICIT` | 공란 | 단계 종료 시간 | 시간 증분 배율, 기본 공란 | 최대 증분 |
| CalculiX 안정화 | `*DYNAMIC, ALPHA=-0.3` | 초기 증분 | 단계 종료 시간 | 최소 증분 | 최대 증분 |

예를 들어 최대 증분 0.00001 s, 종료 시간 0.001 s를 지정하면 CalculiX 낙하는 다음처럼 생성합니다.

```text
*DYNAMIC, EXPLICIT=2
0.0000001, 0.001, 0.000000000001, 0.00001
```

Abaqus 자동 Explicit에서는 다음과 같습니다.

```text
*DYNAMIC, EXPLICIT
, 0.001, , 0.00001
```

최대 증분은 계산 상한입니다. CalculiX 자동 Explicit의 실제 증분은 안정 조건으로 결정되며 입력의 초기 증분 기준값을 그대로 사용하지 않습니다. `FREQUENCY`로 정하는 FRD/DAT 기록 주기 및 결과 프레임 간격과도 다릅니다. 누적 결과창의 전체 시간은 각 낙하·안정화 시간을 합한 값입니다.

## 적용 및 확인

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP을 임시 폴더에 풀고 apply_update.bat을 실행해 기존 설치를 선택합니다.
3. 새 실행을 생성하고 drop_01/calculix_main.inp의 DYNAMIC 데이터 행 및 input_settings.json을 확인합니다.
4. 기존 완료 실행은 입력 해시를 유지하므로 소급 변경하지 않습니다. 기존 버전의 완료 실행을 확인할 때는 그 실행에서 실제 사용한 job.inp를 확인하세요. 원본 template_calculix 및 template_snapshot은 실행 조건의 사본을 덮어쓰는 대상이 아닙니다.

기존 runs·사용자 템플릿·라이브러리·솔버는 보존합니다. 추가 패키지 설치는 없습니다. v0.12.8 출력량 개선을 포함합니다.

## 검증

- 자동 테스트 **220개 통과**.
- 최대 증분/종료 시간 조합 0.00001/0.001, 0.000003/0.007, 자동/0.02를 생성 후 실제 INCLUDE 입력에서 재확인.
- 솔버 호출 직전 조건 재반영, 두 솔버의 Explicit 문법 혼용 차단, 완료된 INCLUDE 실행의 재계산 없는 재변환을 확인.
- Linux CalculiX 2.23에서 짧은 2방향 낙하→안정화를 실제 실행. job.inp→calculix_main.inp 연결로 전 단계 완료, 최종 누적 시간 0.000004 s 및 두 번째 낙하의 native 재료 이력 보존 확인.
- Windows 실환경 및 Abaqus 라이선스 실행은 이번 검증에 포함하지 않았습니다.
