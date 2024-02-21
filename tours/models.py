from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField


class Tour(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    description = models.TextField()
    thumbnail = models.FileField(upload_to='tours_images')
    booking_limit = models.PositiveIntegerField(default=10)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_popular = models.BooleanField(default=False, verbose_name='Popular tour')
    is_featured = models.BooleanField(default=False, verbose_name='Featured tour')
    is_most_visited = models.BooleanField(default=False, verbose_name='Most visited tour')
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
