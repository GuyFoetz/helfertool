# Generated by Django 2.2.11 on 2020-03-24 18:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gifts', '0008_auto_20170401_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='GiftSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enable_automatic_presence', models.BooleanField(default=False, help_text='At the end of the shift, the helper is automatically set to present, unless the absence was reported.', verbose_name='Enable automatic presence for helpers')),
                ('default_deposit', models.IntegerField(blank=True, default=None, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Default deposit for a helper')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registration.Event')),
            ],
        ),
    ]
