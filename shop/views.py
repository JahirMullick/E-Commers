from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    intel = {'no_of_slides':nSlides, 'range': range(nSlides),'product': products}
    return render(request,'shop/index.html', intel)

def about(request):
    return HttpResponse("we are at about")

def contact(request):
    return HttpResponse("we are at contact")

def tracker(request):
    return HttpResponse("we are at tracker")

def search(request):
    return HttpResponse("we are at search")

def productView(request):
    return HttpResponse("we are at product view")

def checkout(request):
    return HttpResponse("we are at checkout")
