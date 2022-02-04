from django.urls import path
from . import views

app_name = 'carts'

urlpatterns = [
    path('', views.cartView, name='cart-view'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name='remove_cart'),
]
