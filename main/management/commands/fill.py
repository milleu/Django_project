from django.core.management import BaseCommand

from main.models import Product, Category


class Command(BaseCommand):

    Product.objects.all().delete()
    Category.objects.all().delete()

    def handle(self, *args, **options):
        product_list = [{"name": "Яблоко",
             "category": "Фрукты",
             "price": 10,
             },
            {"name": "Фундук",
             "category": "Орехи",
             "price": 100,
             },
            {"name": "Огурец",
             "category": "Овощи",
             "price": 15,
             },]
        category_list = [
            {'category': 'Фрукты'},
            {'category': 'Овощи'},
            {'category': 'Орешки'},
        ]

        category_for_create = []
        product_for_create = []
        for product_item in product_list:
           product_for_create.append(Product(**product_item))

        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)