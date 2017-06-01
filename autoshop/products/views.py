# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import render

from autoshop.categories.models import Subcategory, Category
from autoshop.products.models import Product


# Create your views here.
def detail(request, id):
    products = Product.objects.get(id=id)
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'products/detail.html', locals())


def get_products_by_ajax(request):

    cart = request.GET.getlist('ids')
    products = Product.objects.values('id', 'title', 'price', 'discounted_price', 'picture').filter(id__in=cart)
    return JsonResponse(list(products), safe=False)
