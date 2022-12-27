from django.urls import path
from . views import *

app_name = "alumni"

urlpatterns = [
    path("create_alumni/", CreateAlumni.as_view(), name="create_alumni"),
    path("total_alumni/", ListAlumni.as_view(), name="total_alumni"),
    path("all_alumni/", ListAllAlumni.as_view(), name = "all_alumni"),
    path("all_alumni_location/", ListAlumni.as_view(), name="all_alumi_location"),
    path("delete_alumni/<int:pk>/", DeleteAlumni.as_view(), name="delete_alumni"),
    path("update_alumni/<int:pk>/", UpdateAlumni.as_view(), name="update_alumni"),
    path("total_alumni_location/", TotalAlumniLocation.as_view(), name="total_alumni_location"),
    path("get_alumni/<int:pk>/", GetAlumni.as_view(), name="get_alumni")
]