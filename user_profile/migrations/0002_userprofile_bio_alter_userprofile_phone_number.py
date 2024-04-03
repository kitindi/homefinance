# Generated by Django 5.0.3 on 2024-04-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="bio",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.CharField(max_length=255),
        ),
    ]
