# Generated by Django 3.2.18 on 2023-10-10 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("judge", "0171_update_notification"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="rating",
            field=models.IntegerField(db_index=True, default=None, null=True),
        ),
    ]
