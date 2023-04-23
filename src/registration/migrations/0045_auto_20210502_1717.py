# Generated by Django 3.1.8 on 2021-05-02 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("registration", "0044_eventarchive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="link",
            name="creator",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
