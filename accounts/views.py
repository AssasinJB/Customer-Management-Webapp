from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from .models import *

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status = 'delivered').count()
    pending = orders.filter(status = 'Pending').count()
    # print(delivered,pending)
    context = {'customers':customers,'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request,'accounts/dashboard.html',context)

def products(request):
    product = Products.objects.all()
    return render(request,'accounts/products.html',{'products':product})

def customer(request,pk):
    customer = Customer.objects.get(id = pk)

    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {'customer':customer,'orders':orders,'total_orders':total_orders}
    return render(request,'accounts/customer.html',context)