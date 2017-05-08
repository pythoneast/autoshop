# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from autoshop.categories.models import Category, Subcategory

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)