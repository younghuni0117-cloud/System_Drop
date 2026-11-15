# v0.12.7

- Abaqus 새 실행 입력에서 기존 PRODUCT_NODES / PRODUCT_ELEMENTS 집합을 재사용합니다. AUTO_PRODUCT_* 중복 집합은 생성하지 않습니다.
- 제품 전체 노드·요소와 집합 범위가 다르거나 집합이 없으면, 새 실행 폴더의 abaqus_mesh.inp에서만 해당 PRODUCT_* 집합을 보완합니다. 바닥 요소는 포함하지 않습니다.
- 초기속도와 중력, 누적 *IMPORT 입력에도 동일한 집합 이름을 사용합니다. 기존 정상 집합의 GENERATE 또는 하위 집합 참조 형식은 유지합니다.
- main/material/mesh 3개 파일 구조, 원본 템플릿, 이전 runs 및 CalculiX 동작은 유지합니다.
- 추가 라이브러리는 없습니다. Abaqus 실솔버 실행 검증은 라이선스 환경에서 필요합니다.
