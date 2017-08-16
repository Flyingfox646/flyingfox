# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
import django.utils.timezone
import stats.models
import django.contrib.postgres.fields.jsonb
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KillboardPvP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('won_1', models.IntegerField(default=0)),
                ('won_2', models.IntegerField(default=0)),
                ('wl_1', models.FloatField(default=0)),
                ('wl_2', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'killboard_pvp',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('date', models.DateTimeField()),
                ('tik', models.IntegerField(db_index=True)),
                ('type', models.CharField(max_length=16, choices=[('respawn', 'respawn'), ('end', 'end'), ('takeoff', 'takeoff'), ('landed', 'landed'), ('ditched', 'ditched'), ('crashed', 'crashed'), ('bailout', 'bailout'), ('damaged', 'damaged'), ('killed', 'killed'), ('destroyed', 'destroyed'), ('shotdown', 'shotdown')], db_index=True)),
                ('extra_data', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'log_entries',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256, blank=True)),
                ('path', models.CharField(max_length=256, blank=True)),
                ('date_start', models.DateTimeField(db_index=True)),
                ('date_end', models.DateTimeField()),
                ('duration', models.IntegerField(default=0)),
                ('timestamp', models.IntegerField(unique=True)),
                ('players_total', models.IntegerField(default=0)),
                ('pilots_total', models.IntegerField(default=0)),
                ('gunners_total', models.IntegerField(default=0)),
                ('winning_coalition', models.IntegerField(choices=[(1, 'Allies'), (2, 'Axis')], blank=True, null=True)),
                ('win_reason', models.CharField(max_length=8, choices=[('score', 'score'), ('task', 'task')], blank=True)),
                ('preset', models.IntegerField(choices=[(0, 'custom'), (1, 'normal'), (2, 'expert')], default=1)),
                ('settings', django.contrib.postgres.fields.ArrayField(base_field=models.BooleanField(), size=None)),
                ('is_correctly_completed', models.BooleanField(default=False)),
                ('score_dict', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'missions',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('name_en', models.CharField(max_length=64, blank=True, null=True)),
                ('name_ru', models.CharField(max_length=64, blank=True, null=True)),
                ('log_name', models.CharField(max_length=64, unique=True, editable=False)),
                ('cls_base', models.CharField(max_length=24, choices=[('aircraft', 'aircraft'), ('ammo', 'ammo'), ('block', 'block'), ('crew', 'crew'), ('turret', 'turret'), ('vehicle', 'vehicle')], blank=True)),
                ('cls', models.CharField(max_length=24, choices=[('aaa_heavy', 'aaa_heavy'), ('aaa_light', 'aaa_light'), ('aaa_mg', 'aaa_mg'), ('aircraft_gunner', 'aircraft_gunner'), ('aircraft_heavy', 'aircraft_heavy'), ('aircraft_light', 'aircraft_light'), ('aircraft_medium', 'aircraft_medium'), ('aircraft_pilot', 'aircraft_pilot'), ('aircraft_static', 'aircraft_static'), ('aircraft_transport', 'aircraft_transport'), ('aircraft_turret', 'aircraft_turret'), ('armoured_vehicle', 'armoured_vehicle'), ('artillery_field', 'artillery_field'), ('artillery_howitzer', 'artillery_howitzer'), ('artillery_rocket', 'artillery_rocket'), ('block', 'block'), ('bomb', 'bomb'), ('bullet', 'bullet'), ('car', 'car'), ('driver', 'driver'), ('explosion', 'explosion'), ('locomotive', 'locomotive'), ('machine_gunner', 'machine_gunner'), ('parachute', 'parachute'), ('rocket', 'rocket'), ('searchlight', 'searchlight'), ('ship', 'ship'), ('shell', 'shell'), ('tank_heavy', 'tank_heavy'), ('tank_light', 'tank_light'), ('tank_medium', 'tank_medium'), ('trash', 'trash'), ('truck', 'truck'), ('vehicle_crew', 'vehicle_crew'), ('vehicle_static', 'vehicle_static'), ('vehicle_turret', 'vehicle_turret'), ('wagon', 'wagon')], blank=True)),
            ],
            options={
                'verbose_name': 'object',
                'verbose_name_plural': 'objects',
                'db_table': 'objects',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=8, choices=[('pilot', 'pilot'), ('gunner', 'gunner')], db_index=True, default='pilot')),
                ('date_first_sortie', models.DateTimeField(null=True)),
                ('date_last_sortie', models.DateTimeField(null=True)),
                ('date_last_combat', models.DateTimeField(null=True)),
                ('score', models.IntegerField(db_index=True, default=0)),
                ('rating', models.IntegerField(db_index=True, default=0)),
                ('ratio', models.FloatField(default=1)),
                ('sorties_total', models.IntegerField(default=0)),
                ('sorties_coal', django.contrib.postgres.fields.ArrayField(default=stats.models.default_coal_list, base_field=models.IntegerField(default=0), size=None)),
                ('sorties_cls', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_sorties_cls)),
                ('coal_pref', models.IntegerField(choices=[(0, 'neutral'), (1, 'Allies'), (2, 'Axis')], default=0)),
                ('flight_time', models.IntegerField(db_index=True, default=0)),
                ('ammo', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_ammo)),
                ('accuracy', models.FloatField(db_index=True, default=0)),
                ('streak_current', models.IntegerField(db_index=True, default=0)),
                ('streak_max', models.IntegerField(default=0)),
                ('score_streak_current', models.IntegerField(db_index=True, default=0)),
                ('score_streak_max', models.IntegerField(default=0)),
                ('streak_ground_current', models.IntegerField(db_index=True, default=0)),
                ('streak_ground_max', models.IntegerField(default=0)),
                ('bailout', models.IntegerField(default=0)),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
                ('captured', models.IntegerField(default=0)),
                ('relive', models.IntegerField(default=0)),
                ('takeoff', models.IntegerField(default=0)),
                ('landed', models.IntegerField(default=0)),
                ('ditched', models.IntegerField(default=0)),
                ('crashed', models.IntegerField(default=0)),
                ('in_flight', models.IntegerField(default=0)),
                ('shotdown', models.IntegerField(default=0)),
                ('respawn', models.IntegerField(default=0)),
                ('disco', models.IntegerField(default=0)),
                ('ak_total', models.IntegerField(db_index=True, default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(db_index=True, default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('killboard_pvp', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('killboard_pve', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('ce', models.FloatField(default=0)),
                ('kd', models.FloatField(db_index=True, default=0)),
                ('kl', models.FloatField(default=0)),
                ('ks', models.FloatField(default=0)),
                ('khr', models.FloatField(db_index=True, default=0)),
                ('gkd', models.FloatField(default=0)),
                ('gkl', models.FloatField(default=0)),
                ('gks', models.FloatField(default=0)),
                ('gkhr', models.FloatField(default=0)),
                ('wl', models.FloatField(default=0)),
                ('elo', models.FloatField(default=1000)),
                ('fairplay', models.IntegerField(default=100)),
            ],
            options={
                'db_table': 'players',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='PlayerAircraft',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('score', models.IntegerField(default=0)),
                ('ratio', models.FloatField(default=1)),
                ('sorties_total', models.IntegerField(default=0)),
                ('flight_time', models.IntegerField(default=0)),
                ('ammo', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_ammo)),
                ('accuracy', models.FloatField(default=0)),
                ('bailout', models.IntegerField(default=0)),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
                ('captured', models.IntegerField(default=0)),
                ('relive', models.IntegerField(default=0)),
                ('takeoff', models.IntegerField(default=0)),
                ('landed', models.IntegerField(default=0)),
                ('ditched', models.IntegerField(default=0)),
                ('crashed', models.IntegerField(default=0)),
                ('in_flight', models.IntegerField(default=0)),
                ('shotdown', models.IntegerField(default=0)),
                ('respawn', models.IntegerField(default=0)),
                ('disco', models.IntegerField(default=0)),
                ('ak_total', models.IntegerField(default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('killboard_pvp', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('killboard_pve', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('ce', models.FloatField(default=0)),
                ('kd', models.FloatField(default=0)),
                ('kl', models.FloatField(default=0)),
                ('ks', models.FloatField(default=0)),
                ('khr', models.FloatField(default=0)),
                ('gkd', models.FloatField(default=0)),
                ('gkl', models.FloatField(default=0)),
                ('gks', models.FloatField(default=0)),
                ('gkhr', models.FloatField(default=0)),
                ('wl', models.FloatField(default=0)),
                ('aircraft', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, to='stats.Object')),
                ('player', models.ForeignKey(to='stats.Player', related_name='+', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'players_aircraft',
            },
        ),
        migrations.CreateModel(
            name='PlayerMission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('score', models.IntegerField(db_index=True, default=0)),
                ('ratio', models.FloatField(default=1)),
                ('sorties_total', models.IntegerField(default=0)),
                ('sorties_coal', django.contrib.postgres.fields.ArrayField(default=stats.models.default_coal_list, base_field=models.IntegerField(default=0), size=None)),
                ('coal_pref', models.IntegerField(choices=[(0, 'neutral'), (1, 'Allies'), (2, 'Axis')], default=0)),
                ('flight_time', models.IntegerField(db_index=True, default=0)),
                ('ammo', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_ammo)),
                ('accuracy', models.FloatField(db_index=True, default=0)),
                ('bailout', models.IntegerField(default=0)),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
                ('captured', models.IntegerField(default=0)),
                ('relive', models.IntegerField(default=0)),
                ('takeoff', models.IntegerField(default=0)),
                ('landed', models.IntegerField(default=0)),
                ('ditched', models.IntegerField(default=0)),
                ('crashed', models.IntegerField(default=0)),
                ('in_flight', models.IntegerField(default=0)),
                ('shotdown', models.IntegerField(default=0)),
                ('respawn', models.IntegerField(default=0)),
                ('disco', models.IntegerField(default=0)),
                ('ak_total', models.IntegerField(db_index=True, default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(db_index=True, default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('killboard_pvp', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('killboard_pve', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('ce', models.FloatField(default=0)),
                ('kd', models.FloatField(db_index=True, default=0)),
                ('kl', models.FloatField(default=0)),
                ('ks', models.FloatField(default=0)),
                ('khr', models.FloatField(db_index=True, default=0)),
                ('gkd', models.FloatField(default=0)),
                ('gkl', models.FloatField(default=0)),
                ('gks', models.FloatField(default=0)),
                ('gkhr', models.FloatField(default=0)),
                ('wl', models.FloatField(default=0)),
                ('mission', models.ForeignKey(to='stats.Mission', related_name='+', on_delete=models.CASCADE)),
                ('player', models.ForeignKey(to='stats.Player', related_name='+', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'players_missions',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('uuid', models.UUIDField(unique=True, editable=False)),
                ('nickname', models.CharField(max_length=128, db_index=True)),
                ('is_hide', models.BooleanField(db_index=True, default=False)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
                'db_table': 'profiles',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('key', models.CharField(max_length=24, editable=False)),
                ('value', models.IntegerField(default=0, editable=False)),
                ('custom_value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'score',
                'verbose_name_plural': 'scoring',
                'db_table': 'scoring',
                'ordering': ['key'],
            },
        ),
        migrations.CreateModel(
            name='Sortie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=50)),
                ('date_start', models.DateTimeField(blank=True, null=True)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('flight_time', models.IntegerField(default=0)),
                ('fuel', models.IntegerField(default=100)),
                ('skin', models.CharField(max_length=256, blank=True)),
                ('payload_id', models.IntegerField(default=0)),
                ('weapon_mods_id', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('ammo', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_ammo)),
                ('coalition', models.IntegerField(choices=[(0, 'neutral'), (1, 'Allies'), (2, 'Axis')], default=0)),
                ('country', models.IntegerField(choices=[(0, 'neutral'), (101, 'USSR'), (201, 'Germany')], default=0)),
                ('ak_total', models.IntegerField(default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('killboard_pvp', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('killboard_pve', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('status', models.CharField(max_length=12, choices=[('landed', 'landed'), ('ditched', 'ditched'), ('crashed', 'crashed'), ('shotdown', 'shotdown'), ('not_takeoff', 'not takeoff'), ('in_flight', 'in flight')], default='not_takeoff')),
                ('aircraft_status', models.CharField(max_length=12, choices=[('unharmed', 'unharmed'), ('damaged', 'damaged'), ('destroyed', 'destroyed')], default='unharmed')),
                ('bot_status', models.CharField(max_length=12, choices=[('healthy', 'healthy'), ('wounded', 'wounded'), ('dead', 'dead')], default='healthy')),
                ('is_airstart', models.BooleanField(default=False)),
                ('is_bailout', models.BooleanField(default=False)),
                ('is_captured', models.BooleanField(default=False)),
                ('is_disco', models.BooleanField(default=False)),
                ('ratio', models.FloatField(default=1)),
                ('score', models.IntegerField(default=0)),
                ('score_wo_bonus', models.IntegerField(default=0)),
                ('damage', models.FloatField(default=0)),
                ('wound', models.FloatField(default=0)),
                ('bonus', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('debug', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('aircraft', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.PROTECT, to='stats.Object')),
                ('mission', models.ForeignKey(to='stats.Mission', related_name='sorties_list', on_delete=models.CASCADE)),
                ('player', models.ForeignKey(to='stats.Player', related_name='sorties_list', on_delete=models.CASCADE)),
                ('profile', models.ForeignKey(to='stats.Profile', related_name='+', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'sorties',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32, blank=True)),
                ('title_en', models.CharField(max_length=32, blank=True, null=True)),
                ('title_ru', models.CharField(max_length=32, blank=True, null=True)),
                ('date_start', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('date_end', models.DateTimeField(blank=True, null=True)),
                ('is_ended', models.BooleanField(default=False)),
                ('winning_coalition', models.IntegerField(choices=[(1, 'Allies'), (2, 'Axis')], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'tour',
                'verbose_name_plural': 'tours',
                'db_table': 'tours',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='sortie',
            name='tour',
            field=models.ForeignKey(to='stats.Tour', related_name='sorties', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='playermission',
            name='profile',
            field=models.ForeignKey(to='stats.Profile', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='playeraircraft',
            name='profile',
            field=models.ForeignKey(to='stats.Profile', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='player',
            name='profile',
            field=models.ForeignKey(to='stats.Profile', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='player',
            name='tour',
            field=models.ForeignKey(to='stats.Tour', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='object',
            name='score',
            field=models.ForeignKey(to='stats.Score', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='mission',
            name='tour',
            field=models.ForeignKey(to='stats.Tour', related_name='missions', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='logentry',
            name='act_object',
            field=models.ForeignKey(related_name='+', null=True, to='stats.Object', blank=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='logentry',
            name='act_sortie',
            field=models.ForeignKey(related_name='+', null=True, to='stats.Sortie', blank=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='logentry',
            name='cact_object',
            field=models.ForeignKey(related_name='+', null=True, to='stats.Object', blank=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='logentry',
            name='cact_sortie',
            field=models.ForeignKey(related_name='+', null=True, to='stats.Sortie', blank=True, on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='logentry',
            name='mission',
            field=models.ForeignKey(to='stats.Mission', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='killboardpvp',
            name='player_1',
            field=models.ForeignKey(to='stats.Player', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='killboardpvp',
            name='player_2',
            field=models.ForeignKey(to='stats.Player', related_name='+', on_delete=models.CASCADE),
        ),
        migrations.AlterUniqueTogether(
            name='playermission',
            unique_together=set([('player', 'mission')]),
        ),
        migrations.AlterUniqueTogether(
            name='playeraircraft',
            unique_together=set([('player', 'aircraft')]),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('profile', 'type', 'tour')]),
        ),
        migrations.AlterUniqueTogether(
            name='killboardpvp',
            unique_together=set([('player_1', 'player_2')]),
        ),
    ]
