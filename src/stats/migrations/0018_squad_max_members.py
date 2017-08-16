# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0017_squad_num_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='squad',
            name='max_members',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
