# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-09 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bathrooms', '0020_bathroom_location_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='location_desc',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
