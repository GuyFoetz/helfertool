# Generated by Django 2.2.11 on 2020-03-14 12:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("registration", "0039_migrate_admins"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="event",
            name="admins",
        ),
    ]
