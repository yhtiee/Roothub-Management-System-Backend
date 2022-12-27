from . models import *
from rest_framework import serializers

class NYSCSerializer(serializers.ModelSerializer):
    class Meta:
        model = NYSC
        fields = "__all__"