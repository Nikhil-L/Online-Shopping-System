from django.shortcuts import render
from .models import Product
from django.http import HttpResponse

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products' : products})

def product_details(request, slug):
    #return HttpResponse(slug)
    product = Product.objects.get(slug = slug)
    return render(request, 'products/product_details.html', {'product':product})
