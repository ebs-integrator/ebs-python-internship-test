# Generated by Django 4.2.14 on 2024-09-07 14:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0004_alter_blog_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="category",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="blog.category"
            ),
        ),
        migrations.CreateModel(
            name="Comments",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("text", models.TextField()),
                ("blog", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="blog.blog")),
            ],
        ),
    ]
