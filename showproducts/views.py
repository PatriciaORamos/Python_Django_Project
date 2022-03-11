from django.shortcuts import render
from products.models import Product

# Create your views here.
def showproduct_list(request):
   products = Product.objects.all().order_by('title')
   return render(request, 'products/product_list.html', {'products': products })

def showproduct_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product_detail.html', {'product': product })

