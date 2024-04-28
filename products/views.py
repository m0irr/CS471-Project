from django.shortcuts import render
from .models import Product

def products(request):
    x = Product.objects.all()
    show ={'pro':x}
    return render(request,'products/products.html',show)

def product(request):
    return render(request,'products/product.html')