# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-14 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0028_auto_20190405_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]