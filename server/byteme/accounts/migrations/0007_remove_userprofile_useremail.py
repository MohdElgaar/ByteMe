# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-22 21:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181106_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='userEmail',
        ),
    ]
