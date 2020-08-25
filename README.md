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
