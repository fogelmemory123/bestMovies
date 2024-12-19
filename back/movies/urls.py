from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet

# Create a router and register the MovieViewSet
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include the routes from the router
]
