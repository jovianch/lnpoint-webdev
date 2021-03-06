# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-01 06:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_auto_20180223_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='caption',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('PRE', 'PRE'), ('COMPLETED', 'COMPLETED'), ('HELD', 'HELD'), ('POSTED', 'POSTED'), ('CANCELED', 'CANCELED')], max_length=16),
        ),
    ]
