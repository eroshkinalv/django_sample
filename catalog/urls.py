from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ContactTemplateView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView, CategoryListView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('home/', ProductListView.as_view(), name='home'),
    path('contacts/', ContactTemplateView.as_view(), name='contacts'),

    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/detail/', cache_page(60*5)(ProductDetailView.as_view()), name='product_detail'),

    path('category_list/', CategoryListView.as_view(), name='category'),
    path('category/<int:pk>/detail/', CategoryDetailView.as_view(), name='category_detail'),
]
