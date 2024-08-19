from django.urls import path
from . import views

urlpatterns = [
    path('', views.acceuil, name='home'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),
    path('contact/', views.contact, name='contact'),
    path('shop_single/', views.shop_single, name='shop_single'),
]
