from django.urls import path
from . views import *

app_name = "NYSC"

urlpatterns = [
    path("create_NYSC/", CreateNYSC.as_view(), name="create_NYSC"),
    path("total_NYSC/", GeneralTotalNYSC.as_view(), name="total_NYSC"),
    path("all_NYSC/", ListAllNYSC.as_view(), name = "all_NYSC"),
    path("all_NYSC_location/", ListNYSClocation.as_view(), name="all_NYSC_location"),
    path("delete_NYSC/<int:pk>/", DeleteNYSC.as_view(), name="delete_NYSC"),
    path("update_NYSC/<int:pk>/", UpdateNYSC.as_view(), name="update_NYSC"),
    path("total_NYSC_location/", TotalNYSCLocation.as_view(), name="total_NYSC_location"),
    path("get_NYSC/<int:pk>/", RetrieveNYSC.as_view(), name="get_NYSC")
]