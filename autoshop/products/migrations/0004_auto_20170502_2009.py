# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_discount_newproducts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewProducts',
            new_name='NewProduct',
        ),
    ]