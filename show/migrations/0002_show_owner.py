# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 05:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('show', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='owner',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='o', to=settings.AUTH_USER_MODEL),
        ),
    ]