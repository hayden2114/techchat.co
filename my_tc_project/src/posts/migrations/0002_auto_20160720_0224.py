# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 02:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-timeToRead']},
        ),
    ]
