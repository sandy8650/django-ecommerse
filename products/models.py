from django.db import models
from django.urls import reverse
from category.models import Category


class Product(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/products/')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_product_url(self):
        return reverse('products:product_detail', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color')

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size')


VARIATION_CATEGORY_CHOICE = (
    ('color', 'color'),
    ('size', 'size'),
)

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=VARIATION_CATEGORY_CHOICE)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value
