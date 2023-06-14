from rest_framework import serializers
from .models import JbDate
from datetime import datetime, timedelta

class JobSerializer(serializers.ModelSerializer):


    class Meta:
        model = JbDate
        fields = '__all__'
