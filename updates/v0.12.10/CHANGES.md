# v0.12.10 — CalculiX도 main/material/mesh 3개 입력으로 직접 실행

v0.12.9의 job.inp 진입 파일 방식은 3파일 형식을 유지하려는 요청과 맞지 않아 제거했습니다.

## 새 실행 구조

각 낙하·안정화 폴더의 최상위 INP는 다음 3개입니다.

```text
calculix_main.inp
calculix_material.inp
calculix_mesh.inp
```

- Manager에서 입력한 **최대 증분과 종료 시간**은 runs/doe_calculix_.../drop_XX/**calculix_main.inp**의 DYNAMIC 데이터 행에 반영합니다. 안정화 시간 설정은 release_XX/calculix_main.inp에 반영합니다.
- 실제 실행 명령은 **ccx -i calculix_main**입니다. 새 CalculiX 단계는 job.inp를 생성하지 않습니다. main은 material/mesh를 INCLUDE합니다.
- 예전 실행 명령에 `-i job`이 직접 들어 있어도 Manager는 실제 main의 basename으로 반영합니다. 설정의 `{job}`도 새 실행에서는 calculix_main으로 치환됩니다.
- 솔버 결과는 **calculix_main.frd / calculix_main.dat / calculix_main.sta / calculix_main.rout**, 다음 단계의 입력 상태는 **calculix_main.rin**으로 연결됩니다. 진행률·로그·변환·오류 진단·완료 결과 재사용도 이 이름을 사용합니다.
- 생성 후와 실행 직전에 INCLUDE를 펼친 실제 main을 읽어 시간 설정을 검증합니다. **input_settings.json**에서 expected/actual/passed 및 실제 main 파일 이름을 확인할 수 있습니다.
- 원본 template_calculix와 template_snapshot을 수정하지 않습니다. 원본 템플릿에 적힌 시간은 초기 형식이며, 생성된 실행 main에 Manager 설정을 적용합니다.

첫 낙하는 템플릿의 material/mesh 정의를 사용합니다. 안정화와 다음 낙하는 native RESTART로 누적 상태를 읽습니다. 이때도 3파일 형식은 유지하지만 material/mesh include는 상태를 다시 정의하지 않는 주석 파일입니다. 실제 변형·응력·소성 이력은 calculix_main.rin에서 계승합니다. 재시작에서 초기 메쉬와 물성을 다시 선언하여 누적 상태를 덮어쓰지 않습니다.

Abaqus의 main/material/mesh 3파일 구조는 그대로 유지합니다. v0.12.8 결과 출력량 개선과 v0.12.9 솔버별 시간 필드 검증도 포함합니다.

## 기존 실행 및 적용

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP 전체를 임시 폴더에 풀고 apply_update.bat을 실행해 기존 설치 폴더를 선택합니다.
3. 새 실행을 생성하여 위 3개 INP와 main의 DYNAMIC 데이터 행을 확인합니다.

기존에 완료된 job 형식 실행은 입력·결과를 소급 변경하지 않고 그대로 읽습니다. 이전 실행을 재개하면 완료된 이전 단계의 job.rout에서 새 단계의 calculix_main.rin으로 상태를 연결할 수 있습니다. 직접 파일명을 일괄 변경하거나 완료된 기존 job.inp를 삭제할 필요가 없습니다. 아직 계산하지 않은 준비 단계는 실행 전 새 형식으로 정리합니다.

추가 라이브러리 설치는 없습니다. 기존 사용자 템플릿·runs·라이브러리·솔버를 보존합니다.

## 검증

- 자동 테스트 **225개 통과**. 세 가지 최대 증분/종료 시간 조합, 실제 main 반영, job 진입 파일 없음, 실행 명령, 완료 결과 재사용, 기존 입력 호환을 확인했습니다.
- Linux CalculiX 2.23 실제 짧은 2방향 낙하→안정화: 네 단계 모두 3개 INP만 생성, calculix_main 직접 실행·결과 변환 완료, 최종 누적 시간 0.000004 s 및 다음 낙하의 재료 이력 보존 확인.
- 이전 job 기반 첫 낙하·안정화 완료 결과를 보존하고, 다음 낙하·안정화를 새 calculix_main 형식으로 실행하는 연결 테스트도 완료했습니다.
- Windows 실환경과 Abaqus 라이선스 실행은 이번 실제 검증에 포함하지 않았습니다.
