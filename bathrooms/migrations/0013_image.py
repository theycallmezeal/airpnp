# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bathrooms', '0012_auto_20170401_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('bathroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bathrooms.Bathroom')),
            ],
        ),
    ]
