# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show', '0003_auto_20160915_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='description',
            field=models.TextField(blank=True, default='N/A', max_length=50),
        ),
    ]
