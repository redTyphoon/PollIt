# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-26 23:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='publisher',
            field=models.CharField(default='mastsaha', max_length=255),
            preserve_default=False,
        ),
    ]