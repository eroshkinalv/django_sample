from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_view

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_view/<int:pk>/', products_view, name='products_view'),
]
