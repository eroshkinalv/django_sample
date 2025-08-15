from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm, ProductModeratorForm
from .models import Product, Contact, Category
from .services import get_products_from_cache, sort_products_by_category


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = get_products_from_cache()
        return queryset.filter(checkbox=True)


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')

    def get_form_class(self):
        user = self.request.user

        if user == self.object.owner:
            return ProductForm

        if user.has_perm("product.can_unpublish_products"):
            return ProductModeratorForm

        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/products_view.html'
    context_object_name = 'product'


class ContactTemplateView(TemplateView):
    model = Contact
    fields = ('p_name', 'phone', 'message')
    template_name = 'catalog/contacts.html'
    success_url = reverse_lazy('catalog:contacts')

    def post(self, request):

        if request.method == 'POST':
            contact = Contact()
            contact.p_name = request.POST.get('name')
            contact.phone = request.POST.get('phone')
            contact.message = request.POST.get('message')
            contact.save()
            return HttpResponse('Спасибо за обращение.')
        return render(request, 'contacts.html')


class CategoryListView(ListView):
    model = Category
    template_name = 'catalog/category_list.html'
    context_object_name = 'categories'


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'catalog/category_view.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        return sort_products_by_category(self.object.id)
