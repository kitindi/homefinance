# Generated by Django 5.0.3 on 2024-04-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0002_userprofile_bio_alter_userprofile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]