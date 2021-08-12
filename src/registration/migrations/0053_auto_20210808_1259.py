# Generated by Django 3.2.6 on 2021-08-08 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0052_alter_event_ask_nutrition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='mail_validation',
        ),
        migrations.AddField(
            model_name='helper',
            name='timestamp_validated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='helper',
            name='validated',
            field=models.BooleanField(default=False, verbose_name='E-Mail address was confirmed'),
        ),
    ]