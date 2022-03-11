from django.shortcuts import render, redirect
from .models import Category
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib import messages

# Create your views here.
def category_list(request):
   categories = Category.objects.all().order_by('name')
   return render(request, 'categories/category_list.html', {'categories': categories })

def category_detail(request, name):
    category = Category.objects.get(name=name)
    return render(request, 'categories/category_detail.html', { 'category': category })

@login_required(login_url="/accounts/login/")
def category_create(request):
    if request.method == 'POST':
        form = forms.CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Category add successfuly')
            return redirect('categories:list')
    else:
        form = forms.CreateCategory()
    return render(request, 'categories/category_create.html', { 'form': form })

@login_required(login_url="/accounts/login/")
def category_edit(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        form = forms.CreateCategory(request.POST, instance=category)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Category updated successfuly')
            return redirect('categories:list')
    else:
        form = forms.CreateCategory(instance=category)
    context = { 'form': form }
    return render(request, 'categories/category_edit.html', context)

@login_required(login_url="/accounts/login/")
def category_delete(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'POST':
        category.delete()
        messages.success(request, 'Category removed successfuly')
        return redirect('categories:list')
    else:
        context = { 'category': category }
    return render(request, 'categories/category_delete.html', context)


