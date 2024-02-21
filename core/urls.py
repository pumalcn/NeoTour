from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Tour API",
      default_version='v1',
      description="A tour Packages Booking API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="pumalcn03@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny, ],
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('tours.urls')),
    path('api-listings/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-documentation/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
