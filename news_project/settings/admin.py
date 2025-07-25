from .base import *
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'newsdb'),
        'USER': os.getenv('POSTGRES_USER', 'newsuser'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'newspassword'),
        'HOST': os.getenv('POSTGRES_HOST', 'localhost'),
        'PORT': os.getenv('POSTGRES_PORT', "5432"),
    }
}

# URL конфигурация для админского API
ROOT_URLCONF = 'news_project.urls'

# Настройки REST Framework для администратора
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',  # Только для админов
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}

INSTALLED_APPS += ['django_filters']


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'Введите токен в формате: Token <ваш_токен>'
        }
    },
    'USE_SESSION_AUTH': False,
    'PERSIST_AUTH': True,
}