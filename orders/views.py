from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url = "/accounts/login/")
def order_details(request):
    if 'id' in request.POST:
        return HttpResponse(request.POST.get('id'))
