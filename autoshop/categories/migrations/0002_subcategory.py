# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
            ],
            options={
                'verbose_name_plural': 'subcategories',
            },
        ),
    ]
