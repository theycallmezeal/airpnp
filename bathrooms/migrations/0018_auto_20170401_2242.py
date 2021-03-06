# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 02:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bathrooms', '0017_auto_20170401_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('human_readable_location', models.CharField(max_length=100)),
                ('google_maps_link', models.CharField(max_length=50)),
                ('google_maps_embed', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='google_maps_embed',
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='google_maps_link',
        ),
        migrations.RemoveField(
            model_name='bathroom',
            name='human_readable_location',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
    ]
