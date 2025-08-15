from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получает данные о продукте из кэша. Если кэш пуст, получает данные о продукте из бд"""

    if not CACHE_ENABLED:
        return Product.objects.all()

    key = 'product_list'

    product = cache.get(key)

    if product is not None:
        return product

    product = Product.objects.all()
    cache.set(key, product)
    return product


def sort_products_by_category(category_id):
    """Получает продукты одной категории"""

    products = {}
    products['products'] = Product.objects.filter(category=category_id, checkbox=True)
    return products
