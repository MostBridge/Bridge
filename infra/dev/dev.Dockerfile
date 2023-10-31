FROM python:3.11

WORKDIR /app

COPY requirements/develop.txt .
RUN pip install -r develop.txt --no-cache-dir
RUN git submodule update --init --recursive

COPY . .

WORKDIR ./backend

CMD ["gunicorn", "core.wsgi:application", "--bind", "0:8000" ]
