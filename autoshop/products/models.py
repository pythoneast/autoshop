# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from autoshop.categories.models import Category, Subcategory
from smart_selects.db_fields import ChainedForeignKey

STATUS_CHOICES = (
    ('standard', 'Standard'),
    ('discount', 'Discount'),
    ('new', 'New product'),
    ('day', 'Product of the day')
)


class DiscountManager(models.Manager):
    def get_queryset(self):
        return super(DiscountManager, self).get_queryset().filter(status="discount")


class NewProductManager(models.Manager):
    def get_queryset(self):
        return super(NewProductManager, self).get_queryset().filter(status="new")


class ProductOfTheDayManager(models.Manager):
    def get_queryset(self):
        return super(ProductOfTheDayManager, self).get_queryset().filter(status="day")


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, default='standard', max_length=20)
    updated_at = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategories = ChainedForeignKey(
        Subcategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True,
        on_delete=models.CASCADE,
        blank=True,
        null=True)

    objects = models.Manager()
    discount = DiscountManager()
    new_product = NewProductManager()
    day_product = ProductOfTheDayManager()

    def __unicode__(self):
        return self.title

