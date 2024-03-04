from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='имя')
    description = models.CharField(max_length=1000, verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория' )
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    updated_at = models.DateTimeField(verbose_name='дата последнего изменения', **NULLABLE)


    def __str__(self):
        return f'{self.product_name} {self.description}'


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    category = models.CharField(max_length=100, verbose_name='Наименование категории')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
