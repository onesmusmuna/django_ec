from django.shortcuts import render, redirect
from .models import Product

def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            price=request.POST.get('price'),
            category_id=request.POST.get('category'),
            description=request.POST.get('description')
        )
        return redirect('product_list')
    return render(request, 'products/add_product.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
