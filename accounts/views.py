from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .filters import OrderFilter

# Create your views here.
from .models import *
from .forms import *

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,'Username or password is incorrect')
        
        context = {}
        return render(request,'accounts/login.html',context)

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form  = CreateUserForm()

        if(request.method == "POST"):
            form  = CreateUserForm(request.POST)
            
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created successfully for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request,'accounts/register.htm',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def products(request):
    product = Products.objects.all()
    return render(request,'accounts/products.html',{'products':product})

@login_required(login_url='login')
def customer(request,pk):
    customer = Customer.objects.get(id = pk)

    orders = customer.order_set.all()
    total_orders = orders.count()
    
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs


    context = {'customer':customer,'orders':orders,'total_orders':total_orders,'filter':myFilter}
    return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
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

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_Order(request,pk):

    order = Order.objects.get(id = pk)
    if(request.method == "POST"):
        order.delete()
        return redirect('/')

    context ={'item':order}
    return render(request,'accounts/delete_form.html',context)