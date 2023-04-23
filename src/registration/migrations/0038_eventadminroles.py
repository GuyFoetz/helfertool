# Generated by Django 2.2.11 on 2020-03-14 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration", "0037_auto_20200404_2236"),
    ]

    operations = [
        migrations.CreateModel(
            name="EventAdminRoles",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "roles",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("ADMIN", "Administrator"),
                            ("FRONTDESK", "Front desk"),
                            ("INVENTORY", "Inventory"),
                            ("BADGES", "Badges"),
                        ],
                        default="ADMIN",
                        max_length=250,
                        verbose_name="Role",
                    ),
                ),
                ("event", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="registration.Event")),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
