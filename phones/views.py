from django.shortcuts import render, redirect
from phones import models


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_value = request.GET.get('sort', 'name')
    if sort_value == 'name':
        order_value = 'name'
    elif sort_value == 'min_price':
        order_value = 'price'
    else:
        order_value = '-price'
    template = 'catalog.html'
    phones = models.Phone.objects.all().order_by(order_value)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = models.Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
