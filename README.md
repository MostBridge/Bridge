# Bridge
Bridge service for the Yandex Practicum, Career Tracker

# Содержание


1. [Cведения о команде](#)
2. [Cсылка на Github Pages или иной веб хостинг (если приложение опубликовано)](#)
3. [Подготовка к запуску](#start)

    3.1. [Правила работы с git](#git)

    3.2. [Настройка poetry](#poetry)

    3.3. [Настройка pre-commit](#pre-commit)

    3.4. [Настройка переменных окружения](#env)

    3.5. [Запуск в Docker](#run-docker)
4. [Cтэк технологий](#)
5. [Cсылки на сторонние фреймворки, библиотеки, иконки и шрифты если использовались](#)

<br><br>

# 3. Подготовка к запуску <a id="start"></a>

Примечение: использование Poetry и pre-commit.

## 3.1. Правила работы с git (как делать коммиты и pull request-ы)<a id="git"></a>:

1. Две основные ветки: `master` и `develop`
2. Ветка `develop` — “предрелизная”. Т.е. здесь должен быть рабочий и выверенный код
3. Создавая новую ветку, наследуйтесь от ветки `develop`
4. В `master` находится только production-ready код (CI/CD)
5. Правила именования веток
   - весь новый функционал — `feature/название-функционала`
   - исправление ошибок — `bugfix/название-багфикса`
6. Пушим свою ветку в репозиторий и открываем Pull Request

## 3.2. Poetry (инструмент для работы с виртуальным окружением и сборки пакетов)<a id="poetry"></a>:


Poetry - это инструмент для управления зависимостями и виртуальными окружениями, также может использоваться для сборки пакетов. В этом проекте Poetry необходим для дальнейшей разработки приложения, его установка <b>обязательна</b>.<br>

<details>
 <summary>
 Как скачать и установить?
 </summary>

### Установка:

Установите poetry следуя [инструкции с официального сайта](https://python-poetry.org/docs/#installation).
<details>
 <summary>
 Команды для установки:
 </summary>
Для UNIX-систем и Bash on Windows вводим в консоль следующую команду:

> *curl -sSL https://install.python-poetry.org | python -*
Для WINDOWS PowerShell:

> *(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -*
</details>
<br>
После установки перезапустите оболочку и введите команду

> poetry --version
Если установка прошла успешно, вы получите ответ в формате

> Poetry (version 1.2.0)
Для дальнейшей работы введите команду:

> poetry config virtualenvs.in-project true
Выполнение данной команды необходимо для создания виртуального окружения в
папке проекта.

После предыдущей команды создадим виртуальное окружение нашего проекта с
помощью команды:

> poetry install
Результатом выполнения команды станет создание в корне проекта папки .venv.
Зависимости для создания окружения берутся из файлов poetry.lock (приоритетнее)
и pyproject.toml

Для добавления новой зависимости в окружение необходимо выполнить команду

> poetry add <package_name>
_Пример использования:_

> poetry add starlette
Также poetry позволяет разделять зависимости необходимые для разработки, от
основных.
Для добавления зависимости необходимой для разработки и тестирования необходимо
добавить флаг ***--dev***

> poetry add <package_name> --dev
_Пример использования:_

> poetry add pytest --dev
</details>

<details>
 <summary>
 Порядок работы после настройки
 </summary>

<br>

Чтобы активировать виртуальное окружение, введите команду:

> poetry shell
Существует возможность запуска скриптов и команд с помощью команды без
активации окружения:

> poetry run <script_name>.py
_Примеры:_

> poetry run python script_name>.py
>
> poetry run pytest
>
> poetry run black
Порядок работы в оболочке не меняется. Пример команды для Win:

> python src\run_bot.py
Доступен стандартный метод работы с активацией окружения в терминале с помощью команд:

Для WINDOWS:

> source .venv/Scripts/activate
Для UNIX:

> source .venv/bin/activate
</details>

В этом разделе представлены наиболее часто используемые команды.
Подробнее: https://python-poetry.org/docs/cli/

#### Активировать виртуальное окружение
```shell
poetry shell
```

#### Добавить зависимость
```shell
poetry add <package_name>
```

#### Обновить зависимости
```shell
poetry update
```
## 3.3. Pre-commit (инструмент автоматического запуска различных проверок перед выполнением коммита)<a id="pre-commit"></a>:

<details>
 <summary>
 Настройка pre-commit
 </summary>
<br>
1. Убедиться, что pre-comit установлен:

   ```shell
   pre-commit --version
   ```
2. Настроить git hook скрипт:

   ```shell
   pre-commit install
   ```

Далее при каждом коммите у вас будет происходить автоматическая проверка
линтером, а так же будет происходить автоматическое приведение к единому стилю.
</details>

## 3.4. Настройка переменных окружения <a id="env"></a>

Перед запуском проекта необходимо создать копию файла
```.env.example```, назвав его ```.env``` и установить значение токена бота, базы данных почты и тд.

запуск django-приложения (Без БД) вместе с ботом для локальной разработки:
```shell
# Перейти в директорию c кодовой базой проекта backend/, где лежит manage.py
cd backend/

# Запустить веб-сервер командой
poetry run gunicorn config.asgi:application --reload
```

запуск бота с контейнером PostgreSQL:
```shell
make runbot-db
```

остановка контейнера с PostgreSQL:
```shell
make stopdb
```

остановка контейнера с PostgreSQL и удаление базы данных:
```shell
make deletedb
```

наполнение PostgreSQL тестовыми данными:
```shell
# Not ready yet
make filldb
```


## 3.5 Запуск проекта в Docker <a id="run-docker"></a>

1. Убедиться, что ```docker compose``` установлен:
   ```docker compose --version```
2. Из папки ```infra/dev/``` запустить ```docker-compose```:
   ```shell
   sudo docker-compose -f docker-compose.stage.yaml up
   ```
