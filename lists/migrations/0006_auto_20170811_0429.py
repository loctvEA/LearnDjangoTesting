# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-11 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20170810_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
