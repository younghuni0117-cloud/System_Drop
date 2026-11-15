# v0.12.11 — 낙하 번호와 단계별 CalculiX 결과 파일명

완료된 CalculiX 결과 파일을 다음 이름으로 저장합니다.

| 단계 폴더 | FRD | DAT | native 결과 |
|---|---|---|---|
| drop_01 | drop_01_drop.frd | drop_01_drop.dat | drop_01_drop.rout |
| release_01 | drop_01_release.frd | drop_01_release.dat | drop_01_release.rout |
| drop_02 | drop_02_drop.frd | drop_02_drop.dat | drop_02_drop.rout |
| release_02 | drop_02_release.frd | drop_02_release.dat | drop_02_release.rout |

번호는 방향 ID가 아닌 낙하 순번이며 01, 02, 03처럼 최소 두 자리입니다. STA/CVG/MSG 등 해당 솔버 결과에도 같은 접두어를 적용합니다.

## 입력 구조와 파일명 처리

- INP는 기존대로 calculix_main.inp / calculix_material.inp / calculix_mesh.inp 3개입니다. job.inp나 단계별 INP 복사본은 만들지 않습니다.
- 최대 증분·종료 시간은 calculix_main.inp에 반영합니다.
- CalculiX 실행은 ccx -i calculix_main입니다. CalculiX는 입력 basename으로 결과를 기록하므로 **계산 중에는 calculix_main.*로 기록하고, 정상 종료 직후 단계별 이름으로 변경**합니다. 별도 대용량 복사 없이 같은 폴더에서 이름을 변경합니다.
- 결과 변환·모니터링·완료 결과 재사용·다음 낙하로 전달할 native 결과 경로를 새 이름에 연결합니다. FRD와 DAT를 같은 접두어로 유지하여 적분점 응력도 정상적으로 읽습니다.
- 다음 단계의 calculix_main.rin은 결과가 아닌 솔버 재시작 입력이므로 이름을 유지합니다. 예를 들어 drop_01_release.rout의 누적 상태를 다음 단계의 calculix_main.rin으로 전달합니다.
- 각 단계의 input_settings.json에서 result_basename을 확인할 수 있습니다.
- 이름 변경 시 기존 대상 파일을 덮어쓰지 않습니다. 변경 실패 시 이미 바꾼 파일명을 복원하고 완료 계산 기록을 유지해 재개 시 재계산 없이 다시 처리할 수 있습니다.

기존에 완료된 job.* 또는 calculix_main.* 결과는 소급 변경하지 않고 계속 읽습니다. 이번 업데이트 이후 새로 계산하는 단계부터 적용합니다. Abaqus 출력 파일명은 변경하지 않습니다.

## 적용

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. 업데이트 ZIP 전체를 임시 폴더에 풀고 apply_update.bat으로 기존 설치 폴더를 선택합니다.
3. 새 해석 완료 후 단계 폴더에서 위 결과명을 확인합니다.

추가 패키지 설치는 없습니다. 기존 템플릿·runs·라이브러리·솔버를 보존합니다.

## 검증

- 자동 테스트 **233개 통과**, 파일명 관련 8개 테스트 재확인. 두 자리 번호, DAT/FRD 짝, 입력 파일 보존, 실패 시 복원, 기존 파일 덮어쓰기 방지를 확인했습니다.
- Linux CalculiX 2.23의 짧은 2방향 낙하→안정화를 실제 실행했습니다. 네 단계 모두 3개 INP만 유지하고 새 결과명으로 변환·누적 연결을 완료했습니다. 최종 누적 시간 0.000004 s 및 native 재료 이력 보존을 확인했습니다.
- 완료된 새 이름 결과의 재변환을 재시도하면서 솔버를 실행하지 않고 FRD/DAT/native 해시가 유지되는 것을 확인했습니다.
- Windows 실제 실행과 Abaqus 라이선스 실행은 이번 실제 검증에 포함하지 않았습니다.
