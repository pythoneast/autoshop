# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_product_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='expire_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
