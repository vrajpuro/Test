# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 00:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam_app', '0016_auto_20160610_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='momentthumbnail',
            old_name='photo_base64',
            new_name='thumbnail_base64',
        ),
    ]
