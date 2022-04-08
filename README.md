# api_statistics

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

#### О проекте
api_statistics - микросервис для счетчиков статистики.

Сервис умеет взаимодействовать с клиентом при помощи REST API.

#### Стек реализации:
* Язык: Python 3.9
* Web framework: Django 3.2.12 & DRF 3.13.1
* Database: PostgreSQL

#### Доступные эндпоинты:

```
/statistics/
```
Метод запроса: POST

API создает запись со статистикой

Запрос должен принимать:
- date - дата события (обязательное поле)
- views - количество показов
- clicks - количество кликов
- cost - стоимость кликов (в рублях с точностью до копеек)

```
/statistics/
```
Метод запроса: GET

API выдает список всех обьектов модели Statistics
Метод показа статистики
Принимает на вход:

- from - дата начала периода (включительно)
- to - дата окончания периода (включительно)
Отвечает статистикой, отсортированной по дате

```
/statistics/delete/
```
Метод запроса: DELETE

Удаляет все записи из бд

Что бы протестировать приложение необходимо:

* клонировать репозиторий
* создать файл .env и вставить в него переменные и добавить к ним необходимые значения


```
SECRET_KEY=
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
* перейти в директорию с файлом docker-compose.yaml
* ввести в терминале: 
```
docker-compose up -d --build
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input 
```

#### Aвтор:

Алексей Останин
