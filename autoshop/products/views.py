# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

from autoshop.categories.models import Subcategory, Category
from autoshop.products.models import Product


# Create your views here.
def detail(request, id):
    products = Product.objects.get(id=id)
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'products/detail.html', locals())
