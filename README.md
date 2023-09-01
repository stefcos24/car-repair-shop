# Car Repair Shop

### Instruction to start project
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

### Running local tests and validations
- Before committing run nox validation
```bash
$ nox -s lint tests coverage
```

### Instruction to run Ruff

- Before committing to git run linter, if there is errors resolve it
```bash
$ ruff check .
```

### Local environment configuration

Application can consume environment configuration properties from environment variables or from values 
specified in `.env` file. Later option is more convenient for local development environment and to take 
advantage of this mechanism create a `.env` file in the `car-repair-shop/src` directory.

```bash
## This file provides specification for .env files with environment specific settings.
## When new configuration variables are introduced, document them here first.

# Comma-separated list of host name values.
# Example: www.acme.com,app.acme.com
ALLOWED_HOSTS="localhost,127.0.0.1"

# Controls if application is started in debug mode.
# Supported values: True, False
DEBUG=True

# Secret key used in cryptographic functions.
SECRET_KEY="XlNyEphe5mxDTVyrnIurOZvYsLemBtHnTD3mYQuUAj2PyqMM-unog-20fhZn89TP"

# Password for first superuser with admin permissions.
SUPERUSER_PASSWORD="AppAdmin2023!"

# Password for first test user with staff permissions.
TESTUSER_PASSWORD="TestUser2023!"

# Language code for the default language that should be used in fallback situations.
# Examples: en, de, sl, ...
LANGUAGE_CODE=en-us

# Time zone provided
TIME_ZONE="UTC"

# Time zone off
USE_TZ=False

# Defines the static URL prefix for any assets references from
# the site serving static content.
STATIC_URL="static/"
```

**Note: do not place `.env` file under source control as it may contain secrets that are not supposed to 
be shared.**
