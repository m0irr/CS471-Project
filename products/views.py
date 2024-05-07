from django.shortcuts import render
from .models import Product
x = Product.objects.all()
show ={'pro':x}
def products(request):
    return render(request,'products/products.html',show)
def youtube(request):
    return render(request,'products/youtube.html',{'pro':Product.objects.get(name='YouTube premium')})
def pubg(request):
    return render(request,'products/pubg.html',{'pro':Product.objects.get(name='PUBG')})
def iptv(request):
    return render(request,'products/iptv.html',{'pro':Product.objects.get(name='IPTV')})
def shahid(request):
    return render(request,'products/shahid.html',{'pro':Product.objects.get(name='Shahid Sport VIP')})
def cart(request):
    return render(request,'products/cart.html',show)