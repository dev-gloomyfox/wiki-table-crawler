# wiki-table-crawler

## Requirements
- Python>=3.10
- Poetry>=1.2.2
- [Optional] Pyenv>=2.3.8

## Install
- [Optional] Python Environment Settings(Using pyenv)
```
pyenv install 3.10
```
- Poetry
```
poetry install
```
- Pre Commit
```
poetry shell
pre-commit install
```

## Tools
- pycln
```
pycln .
```
- isort
```
isort .
```
- black
```
black .
```
- pylint
```
pylint **/*.py
```
- pytest
```
pytest
```
- mypy
```
mypy .
```

## Structure
```
wiki-table-crawler
│
├── .github/ - github settings directory
│   ├── CODEOWNER
│   ├── PULL_REQUEST_TEMPLATE.md
├── wiki_table_crawler/ - source code root
│   ├── __init__.py
│   ├── crawler.py - sample code
├── tests/ - test code root
│   ├── __init__.py
│   ├── test_crawler.py - sample test code
├── .gitignore
├── .pre-commit-config.yml - pre-commit configuration file
├── poetry.lock
├── pyproject.toml - project configuration file
├── README.md
```