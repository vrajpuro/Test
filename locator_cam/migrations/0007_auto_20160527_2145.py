# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 21:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locator_cam', '0006_auto_20160527_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moment',
            name='photo',
        ),
        migrations.AddField(
            model_name='photo',
            name='moment',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='locator_cam_app.Moment'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moment',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
