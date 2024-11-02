from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context=context)


def contacts(request):
    if request.method == 'POST':
        return HttpResponse('Спасибо за обращение.')
    return render(request, 'contacts.html')


def products_view(request, pk=17):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'products_view.html', context=context)
