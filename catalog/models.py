from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название товара')
    description = models.TextField(null=True, blank=True, verbose_name='Описание товара')
    image = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='categories', verbose_name='Категория товара')
    price = models.IntegerField(help_text='(укажите цену)', verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    checkbox = models.BooleanField(verbose_name="Опубликовать продукт в каталоге", default=False)

    owner = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ['name']
        permissions = [
            ('can_unpublish_products', 'Can unpublish product'),
        ]


class Contact(models.Model):
    p_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.p_name} ({self.phone}): {self.message} / {self.created_at}'

    class Meta:
        verbose_name = 'обратная связь'
        verbose_name_plural = 'обратная связь'
        ordering = ['created_at']
