# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170502_2108'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('standard', 'Standard'), ('discount', 'Discount'), ('new', 'New product')], default='standard', max_length=20),
        ),
    ]
