from django.urls import path
from . views import *

app_name = "interns"

urlpatterns = [
    path("create_intern/", CreateIntern.as_view(), name="create_intern"),
    path("total_intern/", GeneralTotalIntern.as_view(), name="total_intern"),
    path("all_intern/", ListAllIntern.as_view(), name = "all_intern"),
    path("all_intern_location/", ListInternlocation.as_view(), name="all_intern_location"),
    path("delete_intern/<int:pk>/", DeleteIntern.as_view(), name="delete_intern"),
    path("update_intern/<int:pk>/", UpdateIntern.as_view(), name="update_intern"),
    path("total_intern_location/", TotalInternLocation.as_view(), name="total_intern_location"),
    path("get_intern/<int:pk>/", RetrieveIntern.as_view(), name="get_intern")
]