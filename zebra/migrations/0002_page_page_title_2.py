# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-20 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zebra', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='page_title_2',
            field=models.CharField(default='title_2', max_length=100),
            preserve_default=False,
        ),
    ]