# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-24 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kelas', '0006_auto_20171011_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='openclass',
            options={'ordering': ['-id'], 'verbose_name': 'Open Class', 'verbose_name_plural': 'Open Classes'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tags'},
        ),
    ]
