# Generated by Django 3.2.9 on 2021-11-13 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0005_alter_coronasettings_rules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coronasettings',
            name='rules',
            field=models.CharField(choices=[('2G', '2G'), ('2Gplus', '2G plus'), ('3G', '3G'), ('3Gplus', '3G plus')], default='2G', max_length=20, verbose_name='Admission rules'),
        ),
    ]