# Импортирует модуль serializers из библиотеки rest_framework, который предоставляет классы для создания сериализаторов.
from rest_framework import serializers
from .models import Category, Service, Order

# Сериализаторы преобразуют данные из формата Python в JSON и обратно.
# это позволяет легко передавать данные между клиентом и сервером.

# CategorySerializer - Этот класс будет использоваться для сериализации и десериализации данных модели Category
class CategorySerializer(serializers.ModelSerializer):
    # Вложенный класс Meta, который используется для настройки сериализатора.
    class Meta:
        model = Category
        # Указывает, что все поля модели Category должны быть включены в сериализатор.
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

