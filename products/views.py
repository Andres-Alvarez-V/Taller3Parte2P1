from django.shortcuts import render
from .models import Product

# Create your views here.
def products(request):
    productss = Product.objects.all()
    return render(request, 'products.html', {'productss':productss})