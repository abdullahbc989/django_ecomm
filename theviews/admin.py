from django.contrib import admin
from .models import Product, Brand, Cat

# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Cat)