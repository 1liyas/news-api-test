# 📰 News API

REST API для управления новостями, разработанный с использованием Django и Django REST Framework.

## 🚀 Возможности

- Создание, обновление и удаление новостей (для администратора)
- Просмотр и фильтрация новостей (для пользователей)
- Поддержка тегов, категорий и авторов
- Аутентификация по токену
- Документация Swagger
- Кеширование через Redis
- Развёртывание в Docker

## 🛠️ Технологии

- Python 3.12+
- Django 5.1
- Django REST Framework
- PostgreSQL
- Redis
- Docker
- drf-yasg (Swagger)
- dotenv

## ⚙️ Установка

```bash
git clone https://github.com/1liyas/news-api-test.git
cd news-api-test
cp .env.example .env
docker compose up --build
```

## 🔗 Эндпоинты

### Пользовательский доступ

- Получить список новостей: `GET /api/user/news/`
- Swagger-документация: `/api/user/swagger/`

### Административный доступ

- Создать новость: `POST /api/admin/news/`
- Swagger-документация: `/api/admin/swagger/`
- Получить токен: `POST /api/admin/token/`

Пример запроса для получения токена:

```json
POST /api/admin/token/
{
  "username": "admin",
  "password": "admin"
}
```

## 👤 Автор

- GitHub: [@1liyas](https://github.com/1liyas)