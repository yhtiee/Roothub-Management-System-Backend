from django.urls import path
from . views import *

app_name = "trainers"

urlpatterns = [
    path("create_trainer/", CreateTrainer.as_view(), name="create_trainer"),
    path("total_trainer/", GeneralTotalTriainer.as_view(), name="total_trainer"),
    path("all_trainer/", ListAllTrainer.as_view(), name = "all_trainer"),
    path("all_trainer_location/", ListTrainerLocation.as_view(), name="all_trainer_location"),
    path("delete_trainer/<int:pk>/", DeleteTrainer.as_view(), name="delete_trainer"),
    path("update_trainer/<int:pk>/", UpdateTrainer.as_view(), name="update_trainer"),
    path("total_trainer_location/", TotalTrainerLocation.as_view(), name="total_trainer_location"),
    path("get_trainer/<int:pk>/", RetrieveTrainer.as_view(), name="get_trainer")
]