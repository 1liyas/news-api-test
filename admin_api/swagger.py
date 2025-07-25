from rest_framework.authentication import TokenAuthentication  # Добавить
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Admin API",
        default_version='v1',
        description="Документация для административного API",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[TokenAuthentication],  # <<< Указать
)
