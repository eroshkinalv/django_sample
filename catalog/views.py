from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Product, Contact


class ProductListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    template_name = 'home.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products_view.html'
    context_object_name = 'product'


class ContactTemplateView(TemplateView):
    model = Contact
    fields = ('p_name', 'phone', 'message')
    template_name = 'contacts.html'
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
