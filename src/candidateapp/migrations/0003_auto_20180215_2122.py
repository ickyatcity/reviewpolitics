# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-15 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidateapp', '0002_candidateswiki'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidateswiki',
            options={'get_latest_by': 'fecha_ini_det', 'managed': False},
        ),
    ]
