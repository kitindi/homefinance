# Generated by Django 5.0.3 on 2024-04-03 07:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0004_alter_userprofile_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UserProfile",
            new_name="Profile",
        ),
    ]
