# Generated by Django 5.0.3 on 2024-03-29 20:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0006_alter_expense_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Budget",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "budget_name",
                    models.CharField(max_length=256, null=True, unique=True),
                ),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("amout", models.IntegerField(null=True)),
                (
                    "Category",
                    models.CharField(
                        choices=[
                            ("Education", "Education"),
                            ("Groceries", "Groceries"),
                            ("Transportation", "Transportation"),
                            ("Utilities", "Utilities"),
                            ("Fixed expenses", "Fixed expenses"),
                            ("Savings contributions", "Savings contributions"),
                            ("Shopping", "Shopping"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                ("description", models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Income",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
    ]
