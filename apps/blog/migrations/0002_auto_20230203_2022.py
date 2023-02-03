# Generated by Django 3.2.16 on 2023-02-03 20:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='enabled',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
        ),
    ]
