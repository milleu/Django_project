from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):
    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **options):
        product_list = [
            {'category': 'Фрукты', 'description': 'Сладкие и вкусные'},
            {'category': 'Овощи', 'description': 'Большой выбор разных'},
            {'category': 'Орешки', 'description': 'Калорийные и хрустящие'},
        ]

        category_for_create = []
        for product_item in product_list:
           category_for_create.append(Category(**product_item))

        Category.objects.bulk_create(category_for_create)