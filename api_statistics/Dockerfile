FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /

RUN pip install --upgrade pip

RUN pip3 install -r /requirements.txt --no-cache-dir

COPY . .

RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "api_statistics.wsgi:application", "--bind", "0:8000" ]