from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsUserViewSet, NewsListAPIView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Новости API",
        default_version='v1',
        description="Публичный API для чтения новостей",
        contact=openapi.Contact(email="support@example.com"),  # можно убрать или заменить
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'news', NewsUserViewSet, basename='user-news')

urlpatterns = [
    # Swagger и Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Отдельный ListAPIView (если нужно кеширование или особая логика)
    path('news-list/', NewsListAPIView.as_view(), name='news-list-api'),

    # Вьюсеты через router
    path('', include(router.urls)),
]
