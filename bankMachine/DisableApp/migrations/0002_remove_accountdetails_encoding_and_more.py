# Generated by Django 4.2.6 on 2023-12-09 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DisableApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountdetails',
            name='encoding',
        ),
        migrations.AlterField(
            model_name='accountdetails',
            name='address',
            field=models.TextField(),
        ),
    ]