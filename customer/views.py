from django.shortcuts import render, redirect
from .models import *
from .forms import CustomerForm, CustomerSearchForm, CustomerUpdateForm
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    title = 'Customers'
    context = {
    "title": title,
    }
    return render(request, "home_customer.html",context)

@login_required
def add_customer(request):
    form = CustomerForm(request.POST or None)
    total_customers = Customer.objects.count()
    queryset = Customer.objects.order_by('-customer_id')[:6]
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/customer/list_customer')
    context = {
        "form": form,
        "title": "Add Customer",
        "total_customers": total_customers,
		"queryset": queryset,
    }
    return render(request, "entry_customer.html", context)

@login_required
def list_customer(request):
    title = 'List of Customers'
    queryset = Customer.objects.all()
    form = CustomerSearchForm(request.POST or None)
    if request.method == 'POST':
    	queryset = Customer.objects.filter(customer_id__icontains=form['customer_id'].value(),
    									name__icontains=form['name'].value()
    									)
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_customer.html", context)

@login_required
def update_customer(request, pk):
    queryset = Customer.objects.get(customer_id=pk)
    form = CustomerUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = CustomerUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/customer/list_customer')

    context = {
        'form':form
    }
    return render(request, 'entry_customer.html', context)

@login_required
def delete_customer(request, pk):
    queryset = Customer.objects.get(customer_id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/customer/list_customer')
    return render(request, 'delete_customer.html')
