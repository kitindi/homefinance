# Generated by Django 5.0.3 on 2024-03-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_expense_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="payment_method",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
