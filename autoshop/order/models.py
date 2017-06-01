# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from autoshop.products.models import Product
from autoshop.users.models import User


class Order(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User)
    amount = models.PositiveIntegerField(default=0)
    sum = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    address = models.TextField()
