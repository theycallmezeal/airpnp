# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bathrooms', '0006_auto_20170401_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='size_rating',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='smell_rating',
            field=models.PositiveSmallIntegerField(default=3),
            preserve_default=False,
        ),
    ]
