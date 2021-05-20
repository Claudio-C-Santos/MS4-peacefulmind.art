from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """ This view displays all products available """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This view displays the selected product's details"""

    product = get_object_or_404(Product, pk=product_id) 

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
