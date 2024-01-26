# Generated by Django 4.2.4 on 2024-01-25 13:33

import ChabokJobWebsite.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobOffer",
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
                ("title", models.CharField(max_length=256)),
                ("company_name", models.CharField(max_length=128)),
                ("location", models.CharField(max_length=128)),
                ("type_collabration", models.CharField(max_length=128)),
                (
                    "job_description",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                (
                    "reqired_skils",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
                (
                    "company_description",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resume",
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
                    "file_url",
                    models.FileField(
                        default=None,
                        null=True,
                        upload_to=ChabokJobWebsite.models.user_directory_path,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "user_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "role",
                    models.IntegerField(
                        choices=[(0, "EMPLOYER"), (1, "JOB_SEEKER")], default=1
                    ),
                ),
                (
                    "gender",
                    models.IntegerField(
                        blank=True,
                        choices=[(0, "MALE"), (1, "FEMALE")],
                        default=None,
                        null=True,
                    ),
                ),
                ("age", models.IntegerField()),
                (
                    "image",
                    models.ImageField(
                        default=None,
                        null=True,
                        upload_to=ChabokJobWebsite.models.user_directory_path,
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True, default=None, max_length=128, null=True
                    ),
                ),
                (
                    "city",
                    models.CharField(
                        blank=True, default=None, max_length=128, null=True
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user",
                        to="ChabokJobWebsite.resume",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            bases=("auth.user",),
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=128)),
                (
                    "job_offer",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tags",
                        to="ChabokJobWebsite.joboffer",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="tags",
                        to="ChabokJobWebsite.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
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
                    "status",
                    models.IntegerField(
                        choices=[(-1, "REJECTED"), (0, "WAITING"), (1, "ACCEPTED")],
                        default=0,
                    ),
                ),
                (
                    "job_offer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="applications",
                        to="ChabokJobWebsite.joboffer",
                    ),
                ),
                (
                    "resume",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="applications",
                        to="ChabokJobWebsite.resume",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="applications",
                        to="ChabokJobWebsite.user",
                    ),
                ),
            ],
        ),
    ]