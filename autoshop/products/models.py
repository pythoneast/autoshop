# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    picture = models.ImageField(upload_to='products/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    description = models.TextField()

    def __unicode__(self):
        return self.title

