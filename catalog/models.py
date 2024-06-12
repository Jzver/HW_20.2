from django.db import models

NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    category_description = models.TextField(verbose_name='Описание категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    product_description = models.TextField(verbose_name='Описание продукта')
    imagery = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория', related_name="products")
    cost_product = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.category} {self.cost_product}'
