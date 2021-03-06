# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0004_wagondrawing_wagon_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='wagondrawing',
            name='daycolor',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='wagondrawing',
            name='gfnr',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='wagondrawing',
            name='position',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='wagondrawing',
            name='product_description',
            field=models.CharField(blank=True, max_length=82),
        ),
        migrations.AddField(
            model_name='wagondrawing',
            name='sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='wagondrawing',
            name='sortnr',
            field=models.IntegerField(default=0),
        ),
    ]
