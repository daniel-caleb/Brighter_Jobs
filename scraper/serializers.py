from rest_framework import serializers
from .models import Jobs
from datetime import datetime, timedelta

class JobSerializer(serializers.ModelSerializer):


    class Meta:
        model = Jobs
        fields = '__all__'

# class JobFunctionSerializer(serializers.ModelSerializer):   
#     class Meta:
#         model=JobFunctions
#         fields='__all__'