# Generated by Django 3.2.3 on 2021-05-23 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mail", "0007_auto_20190617_1954"),
    ]

    operations = [
        migrations.AlterField(
            model_name="maildelivery",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
        migrations.AlterField(
            model_name="sentmail",
            name="id",
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID"),
        ),
    ]
