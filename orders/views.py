from django.shortcuts import render
from django.http import HttpResponse

def order_details(request):
    return HttpResponse("orders")
