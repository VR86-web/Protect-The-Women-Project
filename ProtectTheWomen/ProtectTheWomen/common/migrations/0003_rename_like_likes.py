# Generated by Django 4.2.16 on 2024-11-25 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        ('common', '0002_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Like',
            new_name='Likes',
        ),
    ]
