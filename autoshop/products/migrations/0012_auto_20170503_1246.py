# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20170503_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]