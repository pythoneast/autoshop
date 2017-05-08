# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from autoshop.categories.models import Category, Subcategory
from autoshop.products.models import Product
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def cat_list(request, cat_id):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    current_category = Category.objects.get(id=cat_id)

    products = Product.objects.filter(category_id=cat_id)
    paginator = Paginator(products, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'categories/category_list.html', locals())


def subcat_list(request, cat_id, subcat_id):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    current_category = Category.objects.get(id=cat_id)
    current_subcategory = Subcategory.objects.get(id=subcat_id)

    products = Product.objects.filter(subcategories=subcat_id)
    paginator = Paginator(products, 3)  # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'categories/category_list.html', locals())