# Generated by Django 5.0.3 on 2024-03-31 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_category_alter_budget_amount_alter_expense_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="amount",
            field=models.IntegerField(null=True),
        ),
    ]
