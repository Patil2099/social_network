# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-09 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='perm_add',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Address'),
        ),
    ]