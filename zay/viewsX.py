from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Produit

# Create your views here.

# views pour ZAY E-COMMERCE

# def acceuil(request):
#     template = loader.get_template('acceuil.html')
#     return HttpResponse(template.render())

# def about(request):
#     template = loader.get_template('about.html')
#     return HttpResponse(template.render())


def acceuil(request):
    return render(request, 'acceuil.html')

def about(request):
    return render(request, 'about.html')

def shop(request):
    return render(request, 'shop.html')

def contact(request):
    return render(request, 'contact.html')









# ******************start views TEST CRUD ************************

def index(request):
    produits = Produit.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        'produits': produits,
    }
    return HttpResponse(template.render(context, request))


def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))


def addrecord(request):
    t = request.POST['titre']
    p = request.POST['prix']
    d = request.POST['description']
    prod = Produit(titre=t, prix=p, description=d)
    prod.save()
    return HttpResponseRedirect(reverse('index'))


def delete(request, id):
    prod = Produit.objects.get(id=id)
    prod.delete()
    return HttpResponseRedirect(reverse('index'))
    

def update(request, id):
    produits = Produit.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'produits': produits,
    }
    return HttpResponse(template.render(context, request))


def updaterecord(request, id):
    t = request.POST['titre']
    p = request.POST['prix']
    d = request.POST['description']
    prod = Produit.objects.get(id=id)
    prod.titre = t
    prod.prix = p
    prod.description = d
    prod.save()
    return HttpResponseRedirect(reverse('index'))

# ********************* End Views TEST CRUD ***********************

