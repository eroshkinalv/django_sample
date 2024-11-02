from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('products_view/<int:pk>/', ProductDetailView.as_view(), name='products_view'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),
]
