# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 21:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='size',
        ),
    ]
