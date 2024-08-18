MANAGE := poetry run python manage.py
PORT ?= 8080

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@poetry install

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: migrate
migrate:
	@$(MANAGE) makemigrations
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	@poetry run flake8 task_manager/

.PHONY: dev
dev:
	@$(MANAGE) runserver

.PHONY: start
start:
	@poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

.PHONY: test
test:
	@$(MANAGE) test -v 2

.PHONY: coverage
coverage:
	@$(MANAGE) 

.PHONY: messages
messages:
	@$(MANAGE) makemessages --locale=ru
