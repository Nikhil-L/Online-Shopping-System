from django.shortcuts import render, redirect
from . import forms

def customer_details(request):
    if request.method == 'POST':
        form = forms.CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:product_list')
    else:
        form = forms.CreateCustomerForm()
    return render(request, 'customer/customer_details.html', {'form':form})
