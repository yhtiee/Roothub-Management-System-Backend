from . models import *
from rest_framework import serializers

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interns
        fields = "__all__"