# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-22 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0003_auto_20160922_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='ABC', max_length=120),
        ),
    ]