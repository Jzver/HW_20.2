import json
from django.core.management import BaseCommand
from django.db import transaction
from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        categories_data = [item for item in data if item.get('model') == "catalog.category"]
        products_data = [item['fields'] for item in data if item.get('model') == "catalog.product"]

        with transaction.atomic():
            self._truncate_tables()
            self._create_categories(categories_data)
            self._create_products(products_data)

    @staticmethod
    def _truncate_tables():
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE;")
            cursor.execute("TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE;")
        Product.objects.all().delete()
        Category.objects.all().delete()

    @staticmethod
    def _create_categories(categories_data):
        category_for_create = [Category(**category) for category in categories_data]
        Category.objects.bulk_create(category_for_create)

    @staticmethod
    def _create_products(products_data):
        categories = Category.objects.in_bulk(field_name='pk')
        product_for_create = [
            Product(
                product_name=product['product_name'],
                product_description=product['product_description'],
                imagery=product['imagery'],
                category=categories[product['category']],
                cost_product=product['cost_product']
            ) for product in products_data
        ]
        Product.objects.bulk_create(product_for_create)
