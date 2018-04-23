# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-29 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20170921_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='first_avatar.png', upload_to=profiles.models.get_avatar_filename),
        ),
    ]
