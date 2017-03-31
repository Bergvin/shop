from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('shop/index.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))
    
def cart(request):
    template = loader.get_template('shop/cart.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))
    
def checkout(request):
    template = loader.get_template('shop/checkout.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))
