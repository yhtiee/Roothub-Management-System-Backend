from django.urls import path
from . views import *

app_name = "trainees"

urlpatterns = [
    path("create_trainee/", CreateTrainee.as_view(), name="create_trainee"),
    path("total_trainee/", GeneralTotalTriainee.as_view(), name="total_trainee"),
    path("all_trainee/", ListAllTrainee.as_view(), name = "all_trainee"),
    path("all_trainee_location/", ListTraineeLocation.as_view(), name="all_trainee_location"),
    path("delete_trainee/<int:pk>/", DeleteTrainee.as_view(), name="delete_trainee"),
    path("update_trainee/<int:pk>/", UpdateTrainee.as_view(), name="update_trainee"),
    path("total_trainee_location/", TotalTraineeLocation.as_view(), name="total_traine_location"),
    path("get_trainee/<int:pk>/", RetrieveTrainee.as_view(), name="get_trainee")
]