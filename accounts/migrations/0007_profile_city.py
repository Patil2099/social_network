# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-09 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_remove_profile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
