# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-30 04:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='oder_id',
            new_name='order_id',
        ),
    ]
