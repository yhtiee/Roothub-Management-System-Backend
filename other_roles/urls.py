from django.urls import path
from . views import *

app_name = "other_roles"

urlpatterns = [
    path("create_otherroles/", CreateOtherRoles.as_view(), name="create_otherroles"),
    path("total_otherroles/", GeneralTotalOtherRoles.as_view(), name="total_otherroles"),
    path("all_otherroles/", ListAllOtherRoles.as_view(), name = "all_otherroles"),
    path("all_otherroles_location/", ListOtherRolesLocation.as_view(), name="all_otherroles_location"),
    path("delete_otherroles/<int:pk>/", DeleteOtherRoles.as_view(), name="delete_otherroles"),
    path("update_otherroles/<int:pk>/", UpdateOtherRoles.as_view(), name="update_otherroles"),
    path("total_otherroles_location/", TotalOtherRolesLocation.as_view(), name="total_otherroles_location"),
    path("get_otherroles/<int:pk>/", RetrieveOtherRoles.as_view(), name="get_otherroles")
]