# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-09 03:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0006_auto_20161009_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payoutsetting',
            name='block_size',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payoutsetting',
            name='reserve',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='payoutsetting',
            name='user_pay_info',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]