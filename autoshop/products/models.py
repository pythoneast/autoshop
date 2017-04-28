# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    picture = models.ImageField()
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()

