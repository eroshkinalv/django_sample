from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Добавьте новый продукт'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Категория 1', description='Описание категории')

        products = [
            {'name': 'Товар 1', 'description': 'Описание товара', 'image': 'image001.jpg', 'category': category, 'price': '1000'},
            {'name': 'Товар 2', 'description': 'Подробное описание товара', 'image': 'image001.jpg', 'category': category, 'price': '2000'},
            {'name': 'Товар 3', 'description': 'Невероятно подробное описание товара', 'image': 'image001.jpg', 'category': category, 'price': '3000'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(
                    self.style.WARNING(f'Student already exists: {product.name}'))
