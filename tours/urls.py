from django.urls import path
from .views import ListTour, RetrieveTour, UpdateTour, DestroyTour, CreateReview, ListBooking, CreateBooking, \
    CreateTour, RetrieveBooking, FilteredTour, ListTourCategory

urlpatterns = [
    path('list-tours/', ListTour.as_view(), name='list-tour'),
    path('create-tour/', CreateTour.as_view(), name='create-tour'),
    path('retrieve-tour/<uuid:pk>/', RetrieveTour.as_view(), name='retrieve-tour'),
    path('update-tour/<uuid:pk>/', UpdateTour.as_view(), name='update-tour'),
    path('destroy-tour/<uuid:pk>/', DestroyTour.as_view(), name='destroy-tour'),
    path('filtered-tours/', FilteredTour.as_view(), name='filtered-tour'),
    path('create-review/', CreateReview.as_view(), name='create-review'),
    path('list-bookings/', ListBooking.as_view(), name='list-booking'),
    path('create-booking/', CreateBooking.as_view(), name='create-booking'),
    path('retrieve-booking/<int:pk>/', RetrieveBooking.as_view(), name='retrieve-booking'),
    path('category-tour/<str:category_name>/', ListTourCategory.as_view(), name='list-tour-category')
]