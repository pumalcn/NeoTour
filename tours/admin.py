from django.contrib import admin

from .models import Tour, Review, Booking, TourCategory

admin.site.register(Tour)
admin.site.register(Review)
admin.site.register(Booking)
admin.site.register(TourCategory)

