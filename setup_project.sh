#!/bin/bash

# Название проекта
PROJECT_NAME="news_project"

echo "✅ Создание виртуального окружения..."
python3 -m venv venv
source venv/bin/activate

echo "✅ Установка зависимостей..."
pip install --upgrade pip
pip install django djangorestframework psycopg2-binary django-filter drf-yasg gunicorn

echo "✅ Создание проекта Django: $PROJECT_NAME"
django-admin startproject $PROJECT_NAME

cd $PROJECT_NAME

echo "✅ Создание приложений admin_api и user_api..."
python manage.py startapp admin_api
python manage.py startapp user_api

echo "✅ Добавление приложений в settings.py..."
sed -i "/INSTALLED_APPS = \[/a \    'rest_framework',\n    'django_filters',\n    'admin_api',\n    'user_api'," $PROJECT_NAME/settings.py

echo "✅ Создание файла requirements.txt..."
pip freeze > ../requirements.txt

cd ..

echo "✅ Создание docker-compose.yml..."
cat <<EOF > docker-compose.yml
version: '3.9'

services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: newsdb
      POSTGRES_USER: adminuser
      POSTGRES_PASSWORD: adminpass
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  web:
    build: .
    command: gunicorn $PROJECT_NAME.wsgi:application --bind 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
    env_file:
      - .env

volumes:
  postgres_data:
EOF

echo "✅ Создание Dockerfile..."
cat <<EOF > Dockerfile
FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /code/
EOF

echo "✅ Создание .env файла..."
cat <<EOF > .env
DJANGO_SECRET_KEY=changeme
DJANGO_DEBUG=True
POSTGRES_DB=newsdb
POSTGRES_USER=adminuser
POSTGRES_PASSWORD=adminpass
EOF

echo "✅ Базовая настройка завершена!"
echo "➡ Теперь можешь запустить:"
echo "    docker-compose up --build"
