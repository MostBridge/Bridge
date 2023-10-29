.SILENT:

COLOR_RESET = \033[0m
COLOR_GREEN = \033[32m
COLOR_YELLOW = \033[33m
COLOR_WHITE = \033[00m

.DEFAULT_GOAL := help


.PHONY: help
help:  # Вызвать help
	@echo -e "$(COLOR_GREEN)Makefile help:"
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "$(COLOR_GREEN)-$$(echo $$l | cut -f 1 -d':'):$(COLOR_WHITE)$$(echo $$l | cut -f 2- -d'#')\n"; done


start-db: # Запуск контейнера Postgres
	docker compose up -d; \
	if [ $$? -ne 0 ]; \
    then \
        docker compose up -d; \
		docker compose version; \
    fi


migrate: # Выполнение миграций Django
	poetry run python manage.py migrate

createsuperuser: # Создать супер пользователя
	poetry run python manage.py createsuperuser --noinput

collectstatic:
	poetry run python manage.py collectstatic --no-input

fixtures:
	poetry run python manage.py loaddata fixtures/data.json

server-init: # Базовая команда для запуска БД, миграций, сервиса.
	make migrate collectstatic createsuperuser fixtures
