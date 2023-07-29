# Car Repair Shop

## Instruction to start project
- Install Python 3.10.10 version 
- Upgrade pip with new version
- Install pipx
```bash
$ python -m pip install upgrade pip
```
- Install pipx
```bash
$ pip install pipx
```
- Install poetry if you don't have already installed
```bash
$ pip install pipx
```
- After pipx is installed, now install poetry
```bash
$ pipx install poetry
```
- Go inside `car-repair-shop/src` folder
- Now run poetry to create virtualenv
```bash
$ poetry shell
```
- Install packages needed for car-repair-shop
```bash
$ poetry install
```
- Run migration script for models
```bash
$ python manage.py migrate
```
- Start Django project from src folder and use http://127.0.0.1:8000/
```bash
$ python manage.py runserver
```

## Instruction to run Ruff

- Before committing to git run linter, if there is errors resolve it
```bash
$ ruff check .
```
