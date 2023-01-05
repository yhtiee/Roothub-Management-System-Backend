from django.urls import path
from . views import *

app_name = "other_roles"

urlpatterns = [
    path("create_other_roles/", CreateOtherRoles.as_view(), name="create_otherroles"),
    path("total_other_roles/", GeneralTotalOtherRoles.as_view(), name="total_otherroles"),
    path("all_other_roles/", ListAllOtherRoles.as_view(), name = "all_otherroles"),
    path("all_other_roles_location/", ListOtherRolesLocation.as_view(), name="all_otherroles_location"),
    path("delete_other_roles/<int:pk>/", DeleteOtherRoles.as_view(), name="delete_otherroles"),
    path("update_other_roles/<int:pk>/", UpdateOtherRoles.as_view(), name="update_otherroles"),
    path("total_other_roles_location/", TotalOtherRolesLocation.as_view(), name="total_otherroles_location"),
    path("get_other_roles/<int:pk>/", RetrieveOtherRoles.as_view(), name="get_otherroles")
]