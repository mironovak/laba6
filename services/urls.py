from django.urls import path, include
# используется для автоматического создания маршрутов для представлений на основе классов (ViewSets).
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ServiceViewSet, OrderViewSet

# DefaultRouter,будет использоваться для автоматического создания маршрутов для представлений на основе классов.
router = DefaultRouter()
# Регистрирует представление CategoryViewSet с префиксом URL categories. Это создаст маршруты для всех 
# стандартных операций CRUD (создание, чтение, обновление, удаление) для модели 
router.register(r'categories', CategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    # Определяет маршрут для корневого URL
    path('', include(router.urls)),
]
