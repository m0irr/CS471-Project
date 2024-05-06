from django.urls import path
from . import views

urlpatterns = [
    path('youtube',views.youtube,name='youtube'),
    path('pubg',views.pubg,name='pubg'),
    path('shahid',views.shahid,name='shahid'),
    path('iptv',views.iptv,name='iptv'),
    path('',views.products,name='products'),
]
