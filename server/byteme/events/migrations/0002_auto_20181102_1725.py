# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='abstractReq',
            field=models.TextField(default=None, max_length=3000, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='detailsReq',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='placeReq',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='timeReq',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='titleReq',
            field=models.CharField(default=None, max_length=300, null=True),
        ),
    ]
