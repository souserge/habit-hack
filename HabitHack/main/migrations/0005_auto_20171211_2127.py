# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 20:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20171211_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('MALE', 'M'), ('FEMALE', 'F')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
