# Generated by Django 5.1.1 on 2024-09-11 15:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0005_alter_comments_blog"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="blog",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="blog.blog"
            ),
        ),
    ]
