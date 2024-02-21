# Generated by Django 4.2.10 on 2024-02-21 13:34

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tour",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("location", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("thumbnail", models.FileField(upload_to="tours_images")),
                ("booking_limit", models.PositiveIntegerField(default=10)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("updated_date", models.DateTimeField(auto_now_add=True)),
                (
                    "is_popular",
                    models.BooleanField(default=False, verbose_name="Popular tour"),
                ),
                (
                    "is_featured",
                    models.BooleanField(default=False, verbose_name="Featured tour"),
                ),
                (
                    "is_most_visited",
                    models.BooleanField(
                        default=False, verbose_name="Most visited tour"
                    ),
                ),
                (
                    "region",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("europe", "Europe"),
                            ("asia", "Asia"),
                            ("north_america", "North America"),
                            ("south_america", "South America"),
                            ("africa", "Africa"),
                            ("australia", "Australia"),
                            ("antarctica", "Antarctica"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Region",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                    "reviewer_name",
                    models.CharField(max_length=150, verbose_name="Reviewer name"),
                ),
                ("review_text", models.TextField(verbose_name="Review")),
                (
                    "tour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="tours.tour",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
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
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None, verbose_name="Phone number"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, null=True, verbose_name="Commentaries to trip"
                    ),
                ),
                (
                    "number_of_people",
                    models.PositiveIntegerField(verbose_name="Number of people"),
                ),
                (
                    "tour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bookings",
                        to="tours.tour",
                    ),
                ),
            ],
        ),
    ]
