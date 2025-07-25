from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsAdminViewSet, CategoryAdminViewSet, TagAdminViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny


router = DefaultRouter()
router.register(r'news', NewsAdminViewSet, basename='admin-news')
router.register(r'categories', CategoryAdminViewSet, basename='admin-categories')
router.register(r'tags', TagAdminViewSet, basename='admin-tags')

schema_view = get_schema_view(
    openapi.Info(
        title="Admin API",
        default_version='v1',
        description="Админская часть API для управления новостями",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    authentication_classes=(TokenAuthentication,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('token/', obtain_auth_token, name='token-auth'),
]
