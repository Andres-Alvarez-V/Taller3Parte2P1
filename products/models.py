from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    marca = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/images/')
    