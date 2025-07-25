from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from admin_api.views import CategoryAdminViewSet, TagAdminViewSet

from django.urls import path
from admin_api.swagger import schema_view

# Swagger schema
schema_view = get_schema_view(
    openapi.Info(
        title="Admin API",
        default_version='v1',
        description="Документация для административного API",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[]  # Без авторизации для документации
)

# Основной роутер
router = DefaultRouter()
router.register(r'categories', CategoryAdminViewSet, basename='admin-categories')
router.register(r'tags', TagAdminViewSet, basename='admin-tags')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/admin/', include('admin_api.urls')),  # включает все маршруты admin_api

    # Swagger UI
    path('api/admin/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='admin-swagger-ui'),
    path('api/admin/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='admin-redoc-ui'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
