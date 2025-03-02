# Generated by Django 4.2.17 on 2025-01-15 00:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0201_add_index_submission_problem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="last_access",
            field=models.DateTimeField(
                db_index=True,
                default=django.utils.timezone.now,
                verbose_name="last access time",
            ),
        ),
    ]
