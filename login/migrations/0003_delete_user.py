# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-13 02:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20190313_1010'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
