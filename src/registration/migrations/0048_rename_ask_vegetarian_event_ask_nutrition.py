# Generated by Django 3.2.6 on 2021-08-06 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0047_auto_20210805_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ask_vegetarian',
            new_name='ask_nutrition',
        ),
    ]