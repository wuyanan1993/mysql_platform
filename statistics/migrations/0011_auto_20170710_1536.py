# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-10 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('statistics', '0010_remove_mysqlinstance_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mysqlinstance',
            old_name='instance_port',
            new_name='port',
        ),
    ]
