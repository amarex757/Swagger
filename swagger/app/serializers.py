from rest_framework import serializers
from .models import *

class EmissionSerializer(serializers.ModelSerializer):
    class Meta():
        model = Emissions
        fields = "__all__"