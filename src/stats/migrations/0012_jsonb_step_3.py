# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-15 19:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0011_jsonb_step_2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logentry',
            old_name='extra_data_new',
            new_name='extra_data',
        ),
        migrations.RenameField(
            model_name='mission',
            old_name='score_dict_new',
            new_name='score_dict',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='ammo_new',
            new_name='ammo',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='killboard_pve_new',
            new_name='killboard_pve',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='killboard_pvp_new',
            new_name='killboard_pvp',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='sorties_cls_new',
            new_name='sorties_cls',
        ),
        migrations.RenameField(
            model_name='playeraircraft',
            old_name='ammo_new',
            new_name='ammo',
        ),
        migrations.RenameField(
            model_name='playeraircraft',
            old_name='killboard_pve_new',
            new_name='killboard_pve',
        ),
        migrations.RenameField(
            model_name='playeraircraft',
            old_name='killboard_pvp_new',
            new_name='killboard_pvp',
        ),
        migrations.RenameField(
            model_name='playermission',
            old_name='ammo_new',
            new_name='ammo',
        ),
        migrations.RenameField(
            model_name='playermission',
            old_name='killboard_pve_new',
            new_name='killboard_pve',
        ),
        migrations.RenameField(
            model_name='playermission',
            old_name='killboard_pvp_new',
            new_name='killboard_pvp',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='ammo_new',
            new_name='ammo',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='bonus_new',
            new_name='bonus',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='debug_new',
            new_name='debug',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='killboard_pve_new',
            new_name='killboard_pve',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='killboard_pvp_new',
            new_name='killboard_pvp',
        ),
        migrations.RenameField(
            model_name='sortie',
            old_name='score_dict_new',
            new_name='score_dict',
        ),
    ]
