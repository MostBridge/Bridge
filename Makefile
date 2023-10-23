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
	docker-compose -f infra/dev/docker-compose.local.yaml up -d; \
	if [ $$? -ne 0 ]; \
    then \
        docker compose -f infra/dev/docker-compose.local.yaml up -d; \
		docker compose version; \
    fi

stop-db: # Остановка контейнера Postgres
	docker-compose -f infra/dev/docker-compose.local.yaml down; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f infra/dev/docker-compose.local.yaml down; \
	fi

clear-db: # Очистка БД Postgres
	docker-compose -f infra/dev/docker-compose.local.yaml down --volumes; \
	if [ $$? -ne 0 ]; \
    then \
		docker compose -f infra/dev/docker-compose.local.yaml down --volumes; \
	fi

migrate: # Выполнение миграций Django
	poetry run python backend/manage.py migrate

createsuperuser: # Создать супер пользователя
	poetry run python backend/manage.py createsuperuser --noinput

run-service: # Запуск Django
	@echo -e "$(COLOR_YELLOW)Starting service...$(COLOR_RESET)"
	@cd backend && poetry run gunicorn --bind 0:8000 core.asgi:application --reload && cd .. && \
	echo -e "$(COLOR_GREEN)Service stopped$(COLOR_RESET)"

service: # Запуск Django пока без gunicorn
	@echo -e "$(COLOR_YELLOW)Starting service...$(COLOR_RESET)"
	@cd backend && poetry run python manage.py runserver && cd .. && \
	echo -e "$(COLOR_GREEN)Service stopped$(COLOR_RESET)"

create-profession: # Команда для создания профессий
	poetry run python backend/manage.py create_profession --amount ${amount}

create-contact: # Команда для создания контакта
	poetry run python backend/manage.py create_contacts --amount ${amount}
