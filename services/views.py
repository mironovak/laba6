# предоставляет классы для создания представлений на основе классов (ViewSets).
from rest_framework import viewsets
from .models import Category, Service, Order
from .serializers import CategorySerializer, ServiceSerializer, OrderSerializer

# Представления обрабатывают запросы и возвращают ответы.

# CategoryViewSet, -  Этот класс будет использоваться для обработки запросов и возврата ответов для модели Category.
class CategoryViewSet(viewsets.ModelViewSet):
    # Указывает набор записей (queryset), который будет использоваться для обработки запросов. В данном случае, это все записи модели Category.
    queryset = Category.objects.all()
    # Указывает класс сериализатора, который будет использоваться для сериализации и десериализации данных модели Category.
    serializer_class = CategorySerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
