# Car Repair Shop

## Instruction to start project
- Install Python 3.10.10 version 
- Upgrade pip with new version
```bash
$ python -m pip install upgrade pip
```
- Install virtual env if you don't have it already
```bash
$ python -m pip install virtualenv
```
- Create and activate your virtual env
```bash
$ python -m venv venv
$ source venv/bin/python
```
- To install all packages for project navigate to src directory and run
```bash
$ pip install -r requirements.txt
```
- Run migration script for models
```bash
$ python manage.py migrate
```
- Start Django project and use http://127.0.0.1:8000/
```bash
$ python manage.py runserver
```