# Generated by Django 5.1.6 on 2025-02-15 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="shortenedurl",
            name="device_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
