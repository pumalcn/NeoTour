from rest_framework import serializers
from .models import Tour, Review, Booking
from django.db.models import Sum
from rest_framework.exceptions import ValidationError


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def create(self, validated_data):
        tour = validated_data.get('tour')
        number_of_people = validated_data.get('number_of_people')

        current_bookings = Booking.objects.filter(tour=tour).aggregate(Sum('number_of_people'))  # получили словарь
        current_bookings_sum = current_bookings.get('number_of_people__sum') or 0  # если еще записей нет, то не вернет None

        if current_bookings_sum + number_of_people > tour.booking_limit:
            raise ValidationError('Booking limit for this tour has been exceeded.')

        return Booking.objects.create(**validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = '__all__'



