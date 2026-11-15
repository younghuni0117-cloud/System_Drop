# v0.12.6 — Abaqus 3파일 입력과 현재 프로그램의 runs 경로

## Abaqus 생성 입력

새 실행의 초기 낙하·안정화·후속 낙하는 기본적으로 다음 세 INP로 생성합니다.

```text
drop_01/ (또는 release_01/, drop_02/)
  abaqus_main.inp
  abaqus_material.inp
  abaqus_mesh.inp
```

main이 material/mesh를 *INCLUDE로 연결합니다. GUI 조건과 Field/History 간격은 그대로 반영합니다.
중복된 job.inp를 남기지 않습니다. 실제 실행 명령은 `job=job input=abaqus_main.inp`를 사용합니다.
결과 job.odb 및 이전 단계 oldjob=.../job 규칙은 유지합니다.
키워드 검사와 input_settings.json도 main의 INCLUDE를 펼쳐 실제 전체 입력을 확인합니다.

초기 모델은 기존 material/mesh를 사용합니다. 후속 Import 단계는 mesh 파일에 *IMPORT와
필요한 집합·표면·추가 형상을 두고 main에 절차·접촉·경계/하중 등을 둡니다.
이때 재료/Section 이력은 native Import가 가져오므로 material 파일에는 재정의하지 않는 이유를 안내합니다.
가져온 제품 노드·요소·재료를 새로 중복 정의하지 않습니다.
회사 템플릿에 별도 INCLUDE 의존성이 있으면 해당 의존성 파일도 함께 보존합니다.

기존 실행 폴더에 job.inp가 있으면 해당 입력을 계속 사용합니다. 완료한 예전 실행의 입력이나 이력을
강제로 변환하지 않습니다. CalculiX의 기존 job/native restart 규칙은 이번 변경에서 유지합니다.

## 결과 위치

상세 옵션의 결과 위치는 **현재 프로그램 폴더/runs**이며 읽기 전용으로 표시합니다.
다른 PC/설치 경로에서 저장한 설정·사용자 기본값을 읽어도 이전 절대 경로를 새 결과 위치로 재사용하지 않습니다.
프로그램을 복사해 실행하면 그 복사본의 runs에 새 doe를 생성합니다.

**이전 실행 폴더 열기 / 재개**로 연 기존 계산은 선택한 원래 폴더에서 이어집니다.
기존 결과를 자동 이동하거나 새 runs에 복제하지 않습니다. 새 실행부터 현재 runs 규칙을 적용합니다.

## 적용

1. Manager와 결과창을 닫습니다. 실행 중이면 현재 단계 완료 후 일시정지합니다.
2. ZIP 전체를 새 임시 폴더에 풀고 apply_update.bat을 실행합니다.
3. 기존 start_windows.bat이 있는 설치 폴더를 선택합니다.
4. 다시 실행하여 상세 옵션의 결과 경로를 확인합니다.
5. 새 실행의 방향 셋업 후 abaqus_main/material/mesh와 input_settings.json을 확인합니다.

이전 패치를 모두 포함합니다. 사용자 템플릿, 기존 runs, 라이브러리·솔버는 보존합니다.

## 검증

자동 테스트 207개 통과. 첫 낙하·Standard Import·다음 Explicit Import의 3파일 구조,
펼친 키워드 검사, 실제 제출 input=abaqus_main.inp 인수, 예전 job.inp 호환,
이전 PC의 결과 경로 재설정, 기존 결과 변환/누적 회귀 검사를 포함합니다.
실제 Qt GUI의 Abaqus 미설치 방향 셋업과 조건 검증도 확인했습니다.
실제 Abaqus 라이선스 실행과 Windows 업데이트 도구 실행은 이 환경에서 미검증입니다.
