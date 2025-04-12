# Generated by Django 5.1.3 on 2025-04-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0031_visitor_institution2_idx"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="visitor",
            index=models.Index(
                condition=models.Q(("institution2__isnull", True)),
                fields=["institution2"],
                name="institution2_not_null_idx",
            ),
        ),
    ]
