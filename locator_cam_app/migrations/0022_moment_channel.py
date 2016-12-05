# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-19 18:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam_app', '0021_channel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='moment',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locator_cam_app.Channel'),
        ),
    ]