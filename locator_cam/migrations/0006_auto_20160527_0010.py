# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 00:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam', '0005_auto_20160527_0010'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moment',
            options={'ordering': ['-pub_time']},
        ),
    ]
