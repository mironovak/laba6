"""laba6 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# предоставляет интерфейс для управления моделями.
from django.contrib import admin
from django.urls import path, include
# используются для получения и обновления токенов JWT.
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
# используется для генерации схемы API.
from drf_yasg.views import get_schema_view
# предоставляет классы для описания схемы API.
from drf_yasg import openapi
# используется для создания представлений перенаправления.
from django.views.generic import RedirectView

# Создает представление схемы API с использованием функции get_schema_view.
schema_view = get_schema_view(
    # Описывает метаданные схемы API, включая заголовок, версию и описание.
    openapi.Info(
        title="API для биржи услуг",
        default_version='v1',
        description="API для биржи услуг",
    ),
    # Указывает, что схема должна быть доступна публично.
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('services.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', RedirectView.as_view(url='swagger/', permanent=False), name='index'),  # Перенаправление на Swagger
]

