from django.core.management import BaseCommand

from main.models import Product, Category

class Command(BaseCommand):
    def handle(self, *args, **options):

        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {"category": "Фрукты"},
            {'category': 'Овощи'},
            {'category': 'Орешки'},
        ]

        product_list = [
            {"product_name": "Яблоко",
             "category": 1,
             "price": 10,
             },
            {"product_name": "Фундук",
             "category": 3,
             "price": 100,
             },
            {"product_name": "Огурец",
             "category": 2,
             "price": 15,
             }]
        category_for_create = []
        product_for_create = []
        for category_item in category_list:
                category_for_create.append(Category(**category_item))
            # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        for product_item in product_list:
            pk = product_item["category"]
            category = Category.objects.filter(pk=pk)
            price1 = product_item["price"]
            name1 = product_item["product_name"]
            product_for_create.append(
                Product(product_name=name1,
                        category=category,
                        price=price1))
            # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)