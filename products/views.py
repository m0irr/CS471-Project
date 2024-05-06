from django.shortcuts import render
from .models import Product

def products(request):
    x = Product.objects.all()
    show ={'pro':x}
    return render(request,'products/products.html',show)

def youtube(request):
    return render(request,'products/youtube.html')
def pubg(request):
    return render(request,'products/pubg.html')
def iptv(request):
    return render(request,'products/iptv.html')
def shahid(request):
    return render(request,'products/shahid.html')