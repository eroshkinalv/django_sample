from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        return HttpResponse('Спасибо за обращение.')
    return render(request, 'contacts.html')
