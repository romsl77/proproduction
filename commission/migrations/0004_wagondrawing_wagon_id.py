# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commission', '0003_wagondrawing_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='wagondrawing',
            name='wagon_id',
            field=models.CharField(default='12042017BL1', max_length=32),
            preserve_default=False,
        ),
    ]
