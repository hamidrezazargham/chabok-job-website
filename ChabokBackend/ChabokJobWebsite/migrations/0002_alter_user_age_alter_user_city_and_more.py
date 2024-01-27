# Generated by Django 4.2.4 on 2024-01-27 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ChabokJobWebsite", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="age",
            field=models.IntegerField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.CharField(blank=True, default="", max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="description",
            field=models.CharField(blank=True, default="", max_length=512, null=True),
        ),
    ]
