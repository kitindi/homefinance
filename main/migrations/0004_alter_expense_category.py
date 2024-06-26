# Generated by Django 5.0.3 on 2024-03-24 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_expense_payment_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="category",
            field=models.CharField(
                choices=[
                    ("Education", "Education"),
                    ("Groceries", "Groceries"),
                    ("Transportation", "Transportation"),
                    ("Utilities", "Utilities"),
                    ("Fixed expenses", "Fixed expenses"),
                    ("Savings contributions", "Savings contributions"),
                ],
                max_length=255,
            ),
        ),
    ]
