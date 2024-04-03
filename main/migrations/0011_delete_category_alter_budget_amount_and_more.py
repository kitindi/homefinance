# Generated by Django 5.0.3 on 2024-03-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_budget_owner"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Category",
        ),
        migrations.AlterField(
            model_name="budget",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name="expense",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]