from django.urls import path
from .views import *

urlpatterns = [
    path("popular_courses/", PopularCoursesLocation.as_view(), name="popular_courses")
]
