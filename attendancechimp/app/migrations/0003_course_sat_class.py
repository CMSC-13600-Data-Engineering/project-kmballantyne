# Generated by Django 5.0.3 on 2024-05-11 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_person_universityperson_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="sat_class",
            field=models.BooleanField(default=False),
        ),
    ]
