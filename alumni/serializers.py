from rest_framework import serializers
from .models import *

class AlumniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainees_alumni
        fields = "__all__"