# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 01:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam', '0017_auto_20160610_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moment',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='moment',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
