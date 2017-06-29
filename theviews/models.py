from django.db import models

# Create your models here.

class Product(models.Model):

    pro_title = models.CharField(max_length=100)
    pro_desc = models.TextField(max_length=200)
    pro_cat = models.CharField(max_length=100)
    pro_brand = models.CharField(max_length=100)
    pro_image = models.CharField(max_length=100)
    pro_price = models.IntegerField()

    def __str__(self):
        return self.pro_title

class Brand(models.Model):

    brand_title = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_title

class Cat(models.Model):

    cat_title = models.CharField(max_length=100)
    def __str__(self):
        return self.cat_title
