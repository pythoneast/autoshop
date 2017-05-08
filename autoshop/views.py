from django.shortcuts import render

from autoshop.categories.models import Category, Subcategory
from autoshop.products.models import Product


def index(request):
    products = Product.objects.all()
    discounts = Product.discount.all()
    new_products = Product.new_product.all()
    day_products = Product.day_product.all()
    day_products = day_products.order_by('updated_at')
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'index.html', context={
        'product': products,
        'discount': discounts,
        'new_product': new_products,
        'day_product': day_products,
        'category': categories,
        'subcategory': subcategories,
    })

