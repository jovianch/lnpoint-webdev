# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-03 19:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('activity', '0006_auto_20180319_1606'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set([('user', 'activity')]),
        ),
    ]
