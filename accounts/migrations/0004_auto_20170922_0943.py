# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-22 09:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170922_0910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userfollow',
            options={'ordering': ['-date_followed']},
        ),
    ]
