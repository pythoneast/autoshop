# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20170502_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('objects', 'objects'), ('discount', 'discount'), ('new_product', 'new_product')], default='standard', max_length=20),
        ),
    ]
