# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 15:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomSkill',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar', models.ImageField(default='first_avatar.png', upload_to='profiles')),
                ('bio', models.CharField(blank=True, default='', max_length=200)),
                ('class_description', models.CharField(blank=True, default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ManyToManyField(blank=True, to='profiles.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Skill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='customskill',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile'),
        ),
    ]
