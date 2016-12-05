# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-25 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moment',
            name='thumbnail_base64',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='base64_image_str',
        ),
        migrations.AddField(
            model_name='moment',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='thumbnail_images'),
        ),
        migrations.AddField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, upload_to='moment_images'),
        ),
    ]
