# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-08-10 21:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='name',
            new_name='Username',
        ),
    ]