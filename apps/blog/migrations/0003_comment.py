# Generated by Django 4.2.14 on 2024-09-06 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blog_enabled"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                ("blog", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="blog.blog")),
            ],
        ),
    ]
