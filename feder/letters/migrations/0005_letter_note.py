# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 23:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0004_auto_20170708_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='note',
            field=models.TextField(blank=True, verbose_name='Comments from editor'),
        ),
    ]