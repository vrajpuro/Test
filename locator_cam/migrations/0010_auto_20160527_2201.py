# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam', '0009_auto_20160527_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='moment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='locator_cam.Moment'),
        ),
    ]
