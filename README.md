### Hexlet tests and linter status:
[![Actions Status](https://github.com/Midnight95/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Midnight95/python-project-52/actions)
[![Testing Status](https://github.com/Midnight95/python-project-52/workflows/Python%20CI/badge.svg)](https://github.com/Midnight95/python-project-52/actions/workflows/tests.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/maintainability)](https://codeclimate.com/github/Midnight95/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/test_coverage)](https://codeclimate.com/github/Midnight95/python-project-52/test_coverage)


## Task manager

Task Manager – a task management system similar to http://www.redmine.org/. 
It allows setting tasks, assigning performers, and changing their statuses.
To work with the system, registration and authentication are required.
The deployed project can be viewed here:

https://python-project-52-c0k7.onrender.com/.



### Installation

- Clone the repo and use Makefile- `make install` 

or

- install package directly via `pip3 install git+https://github.com/Midnight95/python-project-52.git`

To work properly this app needs env variables:
- SECRET_KEY - django secret key. If you can't generate it by yoursel use this website - https://djecrety.ir/

Optionaly:
- DEBUG - set to 'True', if you want to enable debug. 
- DATABASE_URL - you need to specify URL to connect to PosgreSQL, otherwise app will create default SQLite database.
