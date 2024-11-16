from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ProductForm
from .models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ProductDetailView(DetailView):
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
