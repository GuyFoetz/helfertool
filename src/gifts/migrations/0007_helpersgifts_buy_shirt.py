# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("gifts", "0006_deservedgiftset_present"),
    ]

    operations = [
        migrations.AddField(
            model_name="helpersgifts",
            name="buy_shirt",
            field=models.BooleanField(default=False, verbose_name="Buy a T-shirt for helper"),
        ),
    ]
