# Generated by Django 4.2.10 on 2024-02-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0002_alter_tour_updated_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="TourCategory",
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
                    "name",
                    models.CharField(
                        choices=[
                            ("popular", "Popular Tour"),
                            ("featured", "Featured Tour"),
                            ("most_visited", "Most Visited Tour"),
                        ],
                        max_length=70,
                        unique=True,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="tour",
            name="is_featured",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="is_most_visited",
        ),
        migrations.RemoveField(
            model_name="tour",
            name="is_popular",
        ),
        migrations.AddField(
            model_name="review",
            name="reviewer_photo",
            field=models.FileField(
                default="https://res.cloudinary.com/dwdz2kvqj/image/upload/v1708520259/samples/woman-on-a-football-field.jpg",
                upload_to="tours_images",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="is_on_promotion",
            field=models.BooleanField(default=False, verbose_name="Promotion tour"),
        ),
        migrations.AddField(
            model_name="tour",
            name="category",
            field=models.ManyToManyField(
                blank=True, related_name="tours", to="tours.tourcategory"
            ),
        ),
    ]
