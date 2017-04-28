# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField()),
                ('picture', models.ImageField(upload_to=b'')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('description', models.TextField()),
            ],
        ),
    ]
