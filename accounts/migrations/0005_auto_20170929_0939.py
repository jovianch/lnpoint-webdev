# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170922_0943'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollow',
            unique_together=set([('who', 'whom')]),
        ),
    ]