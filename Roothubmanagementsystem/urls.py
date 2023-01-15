"""Roothubmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path("trainees/", include("trainees.urls"), name = "trainees"),
    path("auth/", include("authentication.urls"), name = "auth"),
    path("trainers/", include("trainers.urls"), name = "trainers"),
    path("interns/", include("interns.urls"), name = "interns"),
    path("NYSC/", include("NYSC.urls"), name = "NYSC"),
    path("other_roles/", include("other_roles.urls"), name = "other_roles"),
    # path("expenses/", include("expenses.urls"), name = "expenses"),
    path("alumni/", include("alumni.urls"), name = "expenses"),
    path("courses/", include("popular_courses.urls"), name="courses")


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


