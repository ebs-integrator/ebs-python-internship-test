# Generated by Django 4.2.14 on 2024-09-11 09:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="enabled",
            field=models.BooleanField(default=True),
        ),
    ]
