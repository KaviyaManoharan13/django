# Generated by Django 4.2.7 on 2023-11-23 08:56
""" Migrations for Employesss"""
from django.db import migrations, models


class Migration(migrations.Migration):
    """Migrations for Employes"""

    dependencies = [
        ("Employes", "0002_department_myfield"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="myfield",
            field=models.CharField(
                choices=[("1", "green"), ("2", "red")], max_length=256
            ),
        ),
    ]
