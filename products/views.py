from multiprocessing import context
from django.shortcuts import render
from .models import Product
from category.models import Category


def home(request):
    products = Product.objects.all().filter(is_available=True)
    product_count =  products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'products/home.html', context)

def storeView(request):
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'products/store.html', context)

def storeItemView(request, category_slug):
    categories = None
    products = None
    if category_slug != None:
        products = Product.objects.all().filter(category__slug=category_slug, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'products/store.html', context)


def storeDetailView(request, category_slug, product_slug):
    product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)