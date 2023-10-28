FROM python:3.11
RUN apt-get update && apt install -y curl
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry config virtualenvs.in-project true
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install
COPY ./backend .
CMD [ "poetry", "run", "gunicorn", "core.wsgi:application", "--bind", "0:8000" ]
