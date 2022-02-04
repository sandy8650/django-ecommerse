from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.storeView, name='store'),
    path('store/<slug:category_slug>/', views.storeItemView, name='product_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.storeDetailView, name='product_detail'),
]