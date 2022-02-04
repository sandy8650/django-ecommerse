from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'stock', 'created_date', 'modified_date')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)

admin.site.register(Product, ProductAdmin)