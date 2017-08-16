# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-16 23:03
from __future__ import unicode_literals

from django.db import migrations, models
import squads.models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20160321_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='logo',
            field=models.ImageField(blank=True, upload_to=squads.models.squad_logo_path, verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='squad',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about squad'),
        ),
    ]