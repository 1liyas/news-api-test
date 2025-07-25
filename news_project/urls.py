from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # стандартная админка Django
    path('api/admin/', include('admin_api.urls')),  # admin API + swagger
    path('api/user/', include('user_api.urls')),  # пользовательское API
    path('accounts/', include('django.contrib.auth.urls')),  # если используешь
]
