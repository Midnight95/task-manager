### Hexlet tests and linter status:
[![Actions Status](https://github.com/Midnight95/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Midnight95/python-project-52/actions)
[![Testing Status](https://github.com/Midnight95/python-project-52/workflows/Python%20CI/badge.svg)](https://github.com/Midnight95/python-project-52/actions/workflows/tests.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/maintainability)](https://codeclimate.com/github/Midnight95/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/test_coverage)](https://codeclimate.com/github/Midnight95/python-project-52/test_coverage)


## Task manager

Task Manager – a task management system similar to http://www.redmine.org/. 
It allows setting tasks, assigning performers, and changing their statuses.
To work with the system, registration and authentication are required. Built with Django.

The deployed project can be viewed [here](https://python-project-52-c0k7.onrender.com/)



## Getting Started
**Prerequisites**
Ensure you have Python installed on your machine. Also, in case of cloning the repo you'll need Poetry. This project uses Django, so familiarity with Django concepts is beneficial.

```
git clone https://github.com/Midnight95/python-project-52.git
cd python-project-52
make install
```

**Run migrations**:
```
make migrate
```

**Start the server**:
```
make start
```

**or**

- Install package directly with `pip3 install git+https://github.com/Midnight95/python-project-52.git`.

You're on your own when it comes to running the app in this case though.


### Environment Variables
Create .env file inside project directory with this variables:

`SECRET_KEY`: Set your Django secret key. Generate one using [Djecrety](https://djecrety.ir/) if needed.

`DEBUG`: Enable debugging by setting to True. Use False or leave empty for production.

`DATABASE_URL`: Specify the connection string for your PostgreSQL database. Defaults to SQLite.
