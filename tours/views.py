from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Tour, Review
from .serializers import BookingSerializer, TourSerializer, ReviewSerializer
from rest_framework import generics
from drf_spectacular.utils import extend_schema


@extend_schema(summary="List all tours", description="Retrieve a list of all available tours.")
class ListTour(APIView):
    def get(self, request):
        tours = Tour.objects.all()
        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(summary="Create a new tour", description="Create a new tour with the provided information.")
class CreateTour(APIView):
    def post(self, request):
        serializer = TourSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(summary="Retrieve a specific tour", description="Retrieve detailed information about a specific tour.")
class RetrieveTour(APIView):
    def get(self, request, pk):
        try:
            tour = Tour.objects.get(pk=pk)
        except Tour.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = TourSerializer(tour)
        return Response(serializer.data)


@extend_schema(summary="Update a tour", description="Update the information of a specific tour.")
class UpdateTour(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


@extend_schema(summary="Delete a tour", description="Delete a specific tour.")
class DestroyTour(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    lookup_field = 'pk'


@extend_schema(summary="Filter tours", description="Retrieve a list of tours filtered by promotion status or region.")
class FilteredTour(APIView):
    def get(self, request):
        queryset = Tour.objects.all()
        is_on_promotion = request.query_params.get('is_on_promotion')
        region = request.query_params.get('region')

        if is_on_promotion is not None:
            queryset = queryset.filter(is_on_promotion=is_on_promotion.lower() in ['true', '1', 'yes'])
        if region:
            queryset = queryset.filter(region=region)

        serializer = TourSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(summary="List tours by category", description="Retrieve tours based on their category.")
class ListTourCategory(APIView):
    def get(self, request, category_name):
        tours = Tour.objects.filter(category__name=category_name)
        if not tours:
            return Response({"message": "No tours found for the given category or invalid category name."},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = TourSerializer(tours, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(summary="Create a review", description="Submit a review for a tour.")
class CreateReview(APIView):
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(summary="Create a booking", description="Book a tour.")
class CreateBooking(APIView):
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(summary="List all bookings", description="Retrieve a list of all bookings.")
class ListBooking(APIView):
    def get(self, request):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@extend_schema(summary="Retrieve a specific booking", description="Retrieve detailed information about a specific booking.")
class RetrieveBooking(APIView):
    def get(self, request, pk):
        try:
            booking = Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
