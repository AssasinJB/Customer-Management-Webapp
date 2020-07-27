from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory

# Create your views here.
from .models import *
from .forms import *

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

def create_Order(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('product','status'),extra = 10)
    customer = Customer.objects.get(id = pk)
    # form = OrderForm(initial={'customer':customer})
    formset = OrderFormSet(queryset = Order.objects.none(),instance = customer)
    context = {'formset' :formset}

    if(request.method == "POST"):
        print('Printing POST ',request.POST)
        # form  = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    return render(request,'accounts/order_form.html',context)

def update_Order(request,pk):
    
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)

    context = {'form' :form }

    if(request.method == "POST"):
        # print('Printing POST ',request.POST)
        form  = OrderForm(request.POST,instance = order)
        if form.is_valid:
            form.save()
            return redirect('/')

    return render(request,'accounts/order_form.html',context)

def delete_Order(request,pk):

    order = Order.objects.get(id = pk)
    if(request.method == "POST"):
        order.delete()
        return redirect('/')

    context ={'item':order}
    return render(request,'accounts/delete_form.html',context)