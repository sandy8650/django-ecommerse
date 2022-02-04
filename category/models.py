from django.urls import reverse
from django.db import models


class Category(models.Model):
    category_name  = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/category/')


    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.category_name

    def get_url(self):
        return reverse('products:product_by_category', kwargs={'category_slug': self.slug})