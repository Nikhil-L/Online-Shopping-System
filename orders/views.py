from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import Product
from customer.models import Customer
from .models import Orders
from django.contrib.auth.models import User


@login_required(login_url = "/accounts/login/")
def order_details(request):
    if request.method == 'POST':
        product = Product.objects.get(id = request.POST.get('id'))
        if product.items_remaining >= 1:
            customer = Customer.objects.get(UserName = request.user)

            order = Orders( username = request.user,
                            productname = product.name,
                            cost = product.cost,
                            customer_address = customer.Address,
                            city = customer.City,
                            pincode = customer.Pincode,
                            phone = customer.Phone)
            order.save()
            product.items_remaining = product.items_remaining -1
            product.save()
            return redirect('home')
        else:
            return render(request, 'orders/out_of_stock.html')

    else:
        orders = Orders.objects.filter(username = request.user)
        return render(request, 'orders/order_list.html', {'orders': orders})
