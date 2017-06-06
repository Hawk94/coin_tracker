# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-06 08:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0004_auto_20170606_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btc',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='eth',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ltc',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
