from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class TourCategory(models.Model):
    CATEGORY_CHOICES = (
        ('popular', 'Popular Tour'),
        ('featured', 'Featured Tour'),
        ('most_visited', 'Most Visited Tour'),
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=70, choices=CATEGORY_CHOICES, unique=True)

    def __str__(self):
        return f"{self.name}"


class Tour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    category = models.ManyToManyField(TourCategory, related_name='tours', blank=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.FileField(upload_to='tours_images')
    booking_limit = models.PositiveIntegerField(default=10)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_on_promotion = models.BooleanField(default=False, verbose_name="Promotion tour")
    region = models.CharField(max_length=100, choices=(
        ('europe', 'Europe'),
        ('asia', 'Asia'),
        ('north_america', 'North America'),
        ('south_america', 'South America'),
        ('africa', 'Africa'),
        ('australia', 'Australia'),
        ('antarctica', 'Antarctica'),
    ), blank=True, null=True, verbose_name='Region')

    def __str__(self):
        return f'{self.name} - {self.location}'


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    reviewer_photo = models.FileField(upload_to='tours_images', default="https://res.cloudinary.com/dwdz2kvqj/image/upload/v1708520259/samples/woman-on-a-football-field.jpg")
    reviewer_name = models.CharField(max_length=150, verbose_name='Reviewer name')
    review_text = models.TextField(verbose_name='Review')

    def __str__(self):
        return f"Review by {self.reviewer_name} for the tour {self.tour.name}."


class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='bookings')
    phone_number = PhoneNumberField(verbose_name='Phone number')
    comment = models.TextField(verbose_name='Commentaries to trip', blank=True, null=True)
    number_of_people = models.PositiveIntegerField(verbose_name='Number of people')

    def __str__(self):
        return f"Booking for {self.tour.name} for {self.number_of_people} people."
