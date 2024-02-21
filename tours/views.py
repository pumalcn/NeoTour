from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Booking, Tour, Review
from .serializers import BookingSerializer, TourSerializer, ReviewSerializer
from rest_framework import generics


class ListTour(generics.ListAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class CreateTour(generics.CreateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class RetrieveTour(generics.RetrieveAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class UpdateTour(generics.UpdateAPIView):
    queryset = Tour.objects.all()
    serializer_class = TourSerializer


class DestroyTour(generics.DestroyAPIView):
    queryset = Tour.objects.all()
    lookup_field = 'pk'


class FilteredTour(generics.ListAPIView):
    """
        /tours/filtered/?is_popular=true
        /tours/filtered/?is_most_visited=true&region=europe
        /tours/filtered/?is_featured=true

    """
    serializer_class = TourSerializer

    def get_queryset(self):

        queryset = Tour.objects.all()
        is_popular = self.request.query_params.get('is_popular')
        is_most_visited = self.request.query_params.get('is_most_visited')
        is_featured = self.request.query_params.get('is_featured')
        region = self.request.query_params.get('region')

        # Apply filters if the parameters are in the query
        if is_popular is not None:
            queryset = queryset.filter(is_popular=is_popular.lower() in ['true', '1', 'yes'])
        if is_most_visited is not None:
            queryset = queryset.filter(is_most_visited=is_most_visited.lower() in ['true', '1', 'yes'])
        if is_featured is not None:
            queryset = queryset.filter(is_featured=is_featured.lower() in ['true', '1', 'yes'])
        if region is not None and region != '':
            queryset = queryset.filter(region=region)

        return queryset


class CreateReview(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CreateBooking(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class ListBooking(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RetrieveBooking(generics.RetrieveAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer



# class TourList(APIView):
#     def get(self, request):
#         tours = Tour.objects.all()
#         serializer = TourSerializer(tours, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = TourSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ReviewListAPIView(APIView):
#     def get(self, request):
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ReviewSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookingListAPIView(APIView):
#     def get(self, request):
#         bookings = Booking.objects.all()
#         serializer = BookingSerializer(bookings, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data)
#         if serializer.is_valid():
#             try:
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             except ValidationError as e:
#                 return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
