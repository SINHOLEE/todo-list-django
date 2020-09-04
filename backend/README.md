# Todo list by TTD

## 브랜치 규칙

- `master` : `development`에서 Pull Request한 커밋만 반영함
- `development` : `master`에서 분기, 프로젝트 종료시 `master`로 merge
- `<기능이름>`: `development`에서 분기, 하나의 기능이 완성될 때 `development`로 merge
- `document` : `develop`에서 분기, 문서 완성시 `develop`으로 merge

## 커밋 규칙

> [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)을 따릅니다.

- 커밋 메시지에 타입별 머릿말 붙이기

### 가능한 타입명

- `docs` : 문서와 관련된 커밋입니다.
- `feat` : 기능 개발과 관련된 커밋입니다.
- `fix` : 버그 해결과 관련된 커밋입니다.
- `refactor` : 코드 리팩토링과 관련된 커밋입니다.

- `test`: 테스트 코드 관련 커밋입니다. (custom type)

- 참고: https://github.com/woowa-techcamp-2020/market-11/blob/master/CONTRIBUTING.md

### TDD에 대한 의문점
코드를 구현할수록 테스트 또한 점점 복잡해진다. 그리고 반복적인 노력이 아깝게 생각이 들다보니 아래와 같은 의문이 든다.

- 테스트가 지나치게 많은 것이 아닌가.
- 테스트가 일부 중복되는 것 아닌가. 단위 테스트와 기능 테스트 사이에 분명히 중복된 부분이 있다.
- django.core.urlresolvers 불러오는 건 왜 테스트하는가. 이건 Django 프레임워크 테스트, 서드파티 코드 테스트 아닌가.
- 지금까지 선언 한 줄 테스트, 상수값 반환 검사 같은 단위 테스트는 너무나 자명한(당연한) 것들 아닌가.
- home_page = None 같은 코드는 단위 테스트/코딩 반복 과정에서 좀 건너 뛰어도 되는 것 아닌가.
- 실무적으로 정말 이렇게까지 코딩해야 하는가.

TDD 과정에서 이러한 질문을 하는 것은 충분히 가치가 있는 일이다.

### 자명한 함수의 자명한 테스트를 하는 이유
1. 진짜 자명한 함수의 자명한 테스트를 작성하는 것이라면 어차피 입력하는데 얼마 시간 안 걸리니 그냥 입력하자.
2. 구현을 위해 어떤 생각의 흐름, 사고의 과정을 거쳤는지 흔적을 남기려는 이유이다.

출처: https://wikidocs.net/11060