from django.shortcuts import render, redirect
from .models import *
from .forms import InventoryForm, InventorySearchForm, InventoryUpdateForm
from .models import *
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    title = 'Inventory Management'
    context = {
    "title": title,
    }
    return render(request, "home_inventory.html",context)

@login_required
def add_product(request):
    form = InventoryForm(request.POST or None)
    total_products = Inventory.objects.count()
    queryset = Inventory.objects.order_by('-product_number')[:6]
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('/inventory/list_product')
    context = {
        "form": form,
        "title": "New Product",
        "total_products": total_products,
		"queryset": queryset,
    }
    return render(request, "entry_inventory.html", context)

@login_required
def list_product(request):
    title = 'List of Products'
    queryset = Inventory.objects.all()
    form = InventorySearchForm(request.POST or None)
    if request.method == 'POST':
    	queryset = Inventory.objects.filter(product_number__icontains=form['product_number'].value(),
    									title__icontains=form['title'].value()
    									)
    context = {
        "form": form,
        "title": title,
        "queryset": queryset,
    }
    return render(request, "list_product.html", context)

@login_required
def update_product(request, pk):
    queryset = Inventory.objects.get(product_number=pk)
    form = InventoryUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = InventoryUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/inventory/list_product')

    context = {
        'form':form
    }
    return render(request, 'entry_inventory.html', context)

@login_required
def delete_product(request, pk):
    queryset = Inventory.objects.get(product_number=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect('/inventory/list_product')
    return render(request, 'delete_product.html')
