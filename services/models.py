from django.db import models
#  представляет пользователей в системе аутентификации Django.
from django.contrib.auth.models import User

# ТАБЛИЦЫ
# категории услуг
class Category(models.Model): 
    # Определяет поле name типа CharField с максимальной длиной 100 символов и  именем "Название категории".
    # models.CharField: Поле для хранения строковых данных. 
    name = models.CharField(max_length=100, verbose_name='Название категории')
    #  возвращает строковое представление объекта модели.
    def __str__(self):
        return self.name

# услуги, предоставляемые пользователями.
class Service(models.Model):
    # models.CharField: Поле для хранения строковых данных. 
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    # models.TextField: Поле для хранения больших текстовых данных.
    description = models.TextField(verbose_name='Описание услуги')
    # устанавливает внешний ключ к модели Category с каскадным удалением 
    # (если категория удаляется, все связанные услуги также удаляются) 
    # models.ForeignKey: Поле для хранения внешнего ключа, который ссылается на другую модель. Принимает параметр on_delete, 
    # который указывает, что делать с записями, ссылающимися на удаленную запись.
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    provider = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Поставщик услуги')

    def __str__(self):
        return self.title


class Order(models.Model):
    # устанавливает внешний ключ к модели Service с каскадным удалением 
    # (если услуга удаляется, все связанные заказы также удаляются) 
    service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name='Услуга')
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Клиент')
    # автоматически устанавливается на текущую дату и время при создании объекта 
    # DateTimeField - автоматически устанавливается на текущую дату и время при создании заказа.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Заказ на {self.service.title} от {self.client.username}"
