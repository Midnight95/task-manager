### Hexlet tests and linter status:
[![Actions Status](https://github.com/Midnight95/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Midnight95/python-project-52/actions)
[![Testing Status](https://github.com/Midnight95/python-project-52/workflows/Python%20CI/badge.svg)](https://github.com/Midnight95/python-project-52/actions/workflows/tests.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/maintainability)](https://codeclimate.com/github/Midnight95/python-project-52/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/04f3d6c8a1f9ef95c258/test_coverage)](https://codeclimate.com/github/Midnight95/python-project-52/test_coverage)


## Task manager

Task Manager – система управления задачами, подобная http://www.redmine.org/. Она позволяет ставить задачи, назначать исполнителей и менять их статусы. Для работы с системой требуется регистрация и аутентификация. Развернутый проект можно посмотреть тут:
https://python-project-52-c0k7.onrender.com/



### Установка

- Клонируйте репозиторий и используйте Makefile - `make install` 

или

- Устновите пакет напрямую из репозитория при помощи `pip3 install git+https://github.com/Midnight95/python-project-52.git`

Для работы приложения необходимы следующие переменные окружения:
- SECRET_KEY - django secret key. Если не сможете самостоятельно сгенерировать - https://djecrety.ir/

Опционально:
- DEBUG - True для включения дебага
- DATABASE_URL - необходимо указать URL для подключения к PosgreSQL, в противном случае будет использоваться SQLite
- Возможно понадобиться указать DJANGO_SETTINGS_MODULE=task_manager.settings для корректной работы приложения