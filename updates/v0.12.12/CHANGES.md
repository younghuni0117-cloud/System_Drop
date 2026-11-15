# v0.12.12 — 템플릿의 제품 집합 정의 재사용

Manager가 별도 전체 제품 집합을 만드는 대신 템플릿 mesh의 기존 정의를 사용하도록 CalculiX/Abaqus를 정리했습니다.

## 변경 내용

- CalculiX 초기속도는 **PRODUCT_NODES**, 중력과 적분점 응력 출력은 **PRODUCT_ELEMENTS**를 참조합니다.
- 새 main에 AUTO_PRODUCT_NODES / AUTO_PRODUCT_ELEMENTS를 생성하지 않습니다. 안정화와 다음 낙하도 같은 템플릿 집합을 사용하며 native restart에 보존된 집합을 계승합니다.
- Abaqus에서도 mesh의 기존 PRODUCT_* 정의를 자동 확장·재생성하던 처리를 제거했습니다.
- 기존 정의의 GENERATE, 하위 집합 참조 등 표현과 제품 집합 범위를 유지합니다. 일반적인 3파일 템플릿에서는 생성된 첫 낙하 mesh를 다시 작성하지 않습니다.
- 마커 없는 Abaqus 템플릿을 작업 사본으로 변환할 때도 기존 제품 집합을 유지하며 중복 집합을 추가하지 않습니다. Assembly 평탄화가 필요한 경우 기존 집합을 대응시킵니다. 상세 옵션의 매핑에서 기존 제품 NSET/ELSET을 지정할 수도 있습니다.
- Shell 회전속도 0 지정에만 쓰던 AUTO_SHELL_NODES 집합도 추가하지 않고 해당 노드 번호를 직접 참조합니다.

집합이 없거나 제품 전체와 범위가 다르면 템플릿 오류로 안내합니다. Manager가 새 집합을 만들거나 기존 집합에 노드·요소를 추가하지 않습니다. 이는 이전에 일부 누락을 자동 보완하던 동작을 대체합니다. 새 파트를 추가한 경우에는 원본 mesh의 PRODUCT_* 집합 정의에도 포함시키세요. 바닥은 제품 집합에 포함하지 않습니다.

첫 낙하의 집합 정의는 mesh에만 존재합니다. CalculiX의 안정화·다음 낙하는 native restart를 사용하므로 집합과 재료/형상을 다시 선언하지 않습니다. Abaqus Import에서 필요한 집합은 기존 템플릿 정의를 복사해 사용합니다. 누적 변형·응력·소성 이력을 단순 초기 형상으로 재구성하지 않습니다.

## 유지되는 동작

- main/material/mesh 3개 INP 구조와 Manager의 최대 증분·종료 시간 반영.
- 완료 결과 drop_01_drop.frd / drop_01_release.frd 등의 파일명.
- 템플릿의 section/material/tie/contact 정의와 기존 완료 결과 보존.
- 기존 native 상태에 이미 저장된 AUTO_PRODUCT_* 집합은 강제로 제거하지 않습니다. 새로운 입력에서 이를 새로 정의하거나 참조하지 않습니다.

## 적용

1. 현재 단계 완료 후 Manager와 결과창을 닫습니다.
2. ZIP을 임시 폴더에 풀고 apply_update.bat으로 기존 설치에 적용합니다.
3. 새 실행의 main은 PRODUCT_*를 참조하고 첫 낙하 mesh에는 원래 집합 정의가 유지되는지 확인합니다.

이전 완료 입력과 원본 템플릿은 소급 변경하지 않습니다. 새로 셋업하는 입력에 적용합니다. 추가 패키지 설치는 없습니다.

## 검증

- 자동 테스트 **244개 통과**. CalculiX/Abaqus mesh 원본 보존, GENERATE/하위 집합 참조 유지, 집합 누락·부분 집합 시 자동 수정 없이 오류 안내, 마커 없는 Abaqus 및 Assembly 변환을 확인했습니다.
- Linux CalculiX 2.23의 짧은 2방향 낙하→안정화 실제 실행 완료. 네 단계의 native 상태에 PRODUCT_NODES / PRODUCT_ELEMENTS가 존재하고 AUTO_PRODUCT_* 집합이 생성되지 않음을 확인했습니다.
- 첫 낙하의 native co/vold/veold/sti/xstate/ttime 배열은 이전 AUTO 집합을 사용한 동일 조건 해석과 완전히 동일했습니다. 다음 낙하의 재료 이력도 보존했습니다.
- Windows 실환경 및 Abaqus 라이선스 실행은 이번 실제 검증에 포함하지 않았습니다.
