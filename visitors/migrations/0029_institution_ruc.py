# Generated by Django 5.1.3 on 2025-02-10 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visitors", "0028_visitor_institution2"),
    ]

    operations = [
        migrations.AlterField(
            model_name="institution",
            name="ruc",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="institution",
            name="rank",
            field=models.IntegerField(default=0),
        ),

    ]
