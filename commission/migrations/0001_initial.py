# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 13:17
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WagonDrawing',
            fields=[
                ('wagon_number', models.IntegerField(default=0)),
                ('ok_date', models.DateTimeField()),
                ('link', models.CharField(max_length=300)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
    ]