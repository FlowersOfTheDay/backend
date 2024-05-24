# backend

## Setting

### Github Codespace

본 repository는 개발환경의 편리한 설정을 위해 Github의 Codespace를 사용하였습니다.  
따라서 [Github Codespace 설명](https://docs.github.com/ko/codespaces)을 보고 개발/실행을 하는 것이 좋습니다.  

### Poetry

본 repository는 python 라이브러리의 설정을 위해서 Poetry를 사용하고 있습니다.

`poetry install` 을 이용하여 라이브러리 설정을 하시면 됩니다.

만약 Poetry가 생성한 인터프리터를 IDE에서 잡지못한다면,

`poetry config virtualenvs.in-project true`
`poetry config virtualenvs.path "./.venv"`

위의 두 명령어를 실행하고, 라이브러리 설정을 다시하면 됩니다.
