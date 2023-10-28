FROM python:3.11
WORKDIR /app
COPY develop.txt .
RUN pip install -r develop.txt --no-cache-dir
COPY . ./
CMD ["gunicorn", "core.wsgi:application", "--bind", "0:8000" ]
