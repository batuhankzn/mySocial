# Generated by Django 4.2.2 on 2023-07-20 22:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0002_rename_user_userprofile_username"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
