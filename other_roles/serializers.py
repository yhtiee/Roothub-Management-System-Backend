from . models import *
from rest_framework import serializers

class OtherRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Other_roles
        fields = "__all__"