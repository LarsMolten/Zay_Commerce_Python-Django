from django.shortcuts import render
from django.http import HttpResponse
# from django.urls import reverse
from .models import Category, Product



def acceuil(request):
    categories = Category.objects.all()
    produits = Product.objects.all()[:3]
    # print(categories)
    context = {'categories': categories, 'produits': produits}
    return render(request, 'acceuil.html', context)

def about(request):
    return render(request, 'about.html')

def shop(request):
    produits = Product.objects.all()
    return render(request, 'shop.html', {'produits': produits})

def contact(request):
    return render(request, 'contact.html')

def shop_single(request):
    return render(request, 'shop_single.html')


