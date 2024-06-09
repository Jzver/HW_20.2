import json
from django.core.management import BaseCommand
from django.db import connection
from catalog.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def json_read_categories():
        categories = []
        # Здесь мы получаем данные из фикстур с категориями
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if item.get('model') == "catalog.category":
                    categories.append(item)
        return categories

    @staticmethod
    def json_read_products():
        products = []
        # Здесь мы получаем данные из фикстур с продуктами
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                if item.get('model') == "catalog.product":
                    products.append(item['fields'])
        return products

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")
            cursor.execute("TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")

        # Удалите все продукты
        Product.objects.all().delete()
        # Удалите все категории
        Category.objects.all().delete()

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Словарь для хранения категорий
        categories = {category['pk']: Category(
            pk=category['pk'],
            category_name=category['fields']['category_name'],
            category_description=category['fields']['category_description'])
            for category in self.json_read_categories()}

        # Создаем объекты категорий в базе с помощью метода bulk_create()
        Category.objects.bulk_create(categories.values())

        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in self.json_read_products():
            product_for_create.append(Product(
                product_name=product['product_name'],
                product_description=product['product_description'],
                imagery=product['imagery'],
                category=categories[product['category']],
                cost_product=product['cost_product']))

        # Создаем объекты продуктов в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
