from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    intel = {}
    return render(request,'shop/index.html')

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
