# Generated by Django 4.2.16 on 2024-12-01 08:03

import ProtectTheWomen.accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_appuser_groups_appuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='appuser',
            managers=[
                ('objects', ProtectTheWomen.accounts.managers.AppUserManager()),
            ],
        ),
    ]
