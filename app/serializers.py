from rest_framework import serializers
from app.models import *
class CollegeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=College
        fields='__all__'
        