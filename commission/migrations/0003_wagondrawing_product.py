# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0002_auto_20170411_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='wagondrawing',
            name='product',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]