# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0008_auto_20160415_2121"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="gifts",
            field=models.BooleanField(default=False, verbose_name="Manage gifts for helpers"),
        ),
    ]
