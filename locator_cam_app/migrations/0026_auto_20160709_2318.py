# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-09 23:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locator_cam_app', '0025_auto_20160625_2358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('request_message', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChannelInvitation',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locator_cam_app.Request')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator_cam_app.Channel')),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('locator_cam_app.request',),
        ),
        migrations.CreateModel(
            name='ChannelRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locator_cam_app.Request')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locator_cam_app.Channel')),
            ],
            bases=('locator_cam_app.request',),
        ),
        migrations.CreateModel(
            name='FriendRequest',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='locator_cam_app.Request')),
                ('requestee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('locator_cam_app.request',),
        ),
        migrations.AddField(
            model_name='request',
            name='requester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
