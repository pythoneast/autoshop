# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25, unique=True)

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.title


class Subcategory(models.Model):
    title = models.CharField(max_length=25, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "subcategories"

    def __unicode__(self):
        return self.title
