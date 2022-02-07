from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .models import Product
from category.models import Category
from carts.models import CartItem
from carts.views import _cart_id


def home(request):
    products = Product.objects.all().filter(is_available=True)
    product_count =  products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'products/home.html', context)

def storeView(request):
    products = Product.objects.all().filter(is_available=True).order_by('id')
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_product = paginator.get_page(page)
    product_count = products.count()
    context = {
        'products': paged_product,
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
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product)
    except Exception as e:
        raise e
    context = {
        'product': product,
        'in_cart': in_cart,
    }
    return render(request, 'products/product_detail.html', context)

def search_items(request):
    product = None
    product_count = 0
    if 'keyword' in request.path:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(Q(discription__icontains=keyword) | Q(title__icontains=keyword))
            product_count = product.count()
    return render(request, 'products/store.html', {'products': products, 'product_count': product_count,})