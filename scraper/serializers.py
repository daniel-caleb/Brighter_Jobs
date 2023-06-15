from rest_framework import serializers
from .models import Jobs, JobFunctions
from datetime import datetime, timedelta

class JobFunctionSerializer(serializers.ModelSerializer):   
    class Meta:
        model=JobFunctions
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    Job_Function = JobFunctionSerializer()

    class Meta:
        model = Jobs
        fields = ['id', 'job_title', 'scraped_date','job_link', 'Job_Function']
