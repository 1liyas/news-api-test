from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="User API",
        default_version='v1',
        description="Документация для пользовательского API",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Swagger доступен всем
    authentication_classes=[],  # <--- отключаем авторизацию
)