# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-09 04:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='objectviewed',
            options={'ordering': ['-timestamp'], 'verbose_name': 'object viewed', 'verbose_name_plural': 'objects viewed'},
        ),
    ]
