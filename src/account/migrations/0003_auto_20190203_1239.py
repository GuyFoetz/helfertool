# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-03 11:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_auto_20190202_2336"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="agreement",
            name="begin",
        ),
        migrations.AddField(
            model_name="agreement",
            name="start",
            field=models.DateField(default=django.utils.datetime_safe.datetime.now, verbose_name="Start date"),
            preserve_default=False,
        ),
    ]
