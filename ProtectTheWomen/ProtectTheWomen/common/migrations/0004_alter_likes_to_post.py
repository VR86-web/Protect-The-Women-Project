# Generated by Django 4.2.16 on 2024-11-26 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('common', '0003_rename_like_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='to_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.posts'),
        ),
    ]
