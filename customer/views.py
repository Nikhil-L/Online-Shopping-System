from django.shortcuts import render, redirect
from . import forms


def customer_details(request):
    if request.method == 'POST':
        form = forms.CreateCustomerForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.UserName = request.user
            instance.save()
            return redirect('home')
    else:
        form = forms.CreateCustomerForm()
    return render(request, 'customer/customer_details.html', {'form':form})
