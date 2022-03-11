from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages
import os

# Create your views here.
def product_list(request):
   products = Product.objects.all().order_by('title')
   return render(request, 'products/product_list.html', {'products': products })

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product })

@login_required(login_url="/accounts/login/")
def product_create(request):
    if request.method == 'POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            messages.success(request, 'Product add successfuly')
            return redirect('products:list')
    else:
        form = forms.CreateProduct()
    return render(request, 'products/product_create.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def product_edit(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(product.picture) > 0:
                os.remove(product.picture.path)
            product.picture = request.FILES['picture']
        form = forms.CreateProduct(request.POST, instance=product)
        if form.is_valid():
            instance = form.save(commit=False)
            messages.success(request, 'Product updated successfuly')
            instance.save()
            return redirect('products:list')
    else:
        form = forms.CreateProduct(instance=product)
    context = { 'form': form }
    return render(request, 'products/product_edit.html', context)

@login_required(login_url="/accounts/login/")
def product_delete(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product removed successfuly')
        return redirect('products:list')
    else:
        context = { 'product': product }
    return render(request, 'products/product_delete.html', context)


