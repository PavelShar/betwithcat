# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 22:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittySite', '0002_game_finished'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
