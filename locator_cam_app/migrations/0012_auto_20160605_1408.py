# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam_app', '0011_auto_20160605_0442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]