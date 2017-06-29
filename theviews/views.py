from django.shortcuts import render
from .models import Product
from .models import Cat
from .models import Brand
import random
# Create your views here.

def product_list(request):
    products = Product.objects.all()
    cats = Cat.objects.all()
    brands = Brand.objects.all()
    return render(request, 'index.html', {'products': products, 'brands': brands, 'cats': cats})

def details(request, pro_id):
    product = Product.objects.get(id=pro_id)
    return render(request, 'details.html', {'product': product})
