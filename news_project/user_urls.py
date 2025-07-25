from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="User API",
      default_version='v1',
      description="Документация для пользовательского API",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
   authentication_classes=[],  # отключили SessionAuth
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user_api.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # ✅ добавь эту строку для Swagger UI
    path('api/user/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)