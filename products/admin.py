from django.contrib import admin
from .models import Product, Variation


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'stock', 'created_date', 'modified_date')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_date', 'modified_date')
    ordering = ('-created_date',)


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('variation_category', 'variation_value', 'is_active')
    readonly_fields = ('created_date',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)