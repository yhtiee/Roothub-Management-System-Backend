from . models import *
from rest_framework import serializers

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainees_general
        fields = "__all__"