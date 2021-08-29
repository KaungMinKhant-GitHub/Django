from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

from accounts.models import *

def customers(request,id):
    customer = Customers.objects.get(id = id)
    orders = customer.order_set.all()
    order_count = orders.count()

    return render(request,'accounts/customers.html',{
        'customer' : customer,
        'orders' : orders,
        'orders_count' : order_count
    })

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html',{
        'products' : products
    })

def domain(request):
    customers = Customers.objects.all()
    orders = Order.objects.all()
    total = orders.count()
    delivered = Order.objects.filter(status='Delivered').count()
    pending = Order.objects.filter(status='pending').count()

    return render(request,'accounts/domain.html',{
        'customers' : customers,
        'orders' : orders,
        'total' : total,
        'delivered' : delivered,
        'pending' : pending
    })
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               