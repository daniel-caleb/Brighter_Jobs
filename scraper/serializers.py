from rest_framework import serializers
from .models import Jobs, JobFunctions, JobLocation, JobIndustries, JobDetails
from datetime import datetime, timedelta

class JobDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobDetails
        fields='__all__'

class JobFunctionSerializer(serializers.ModelSerializer):   
    class Meta:
        model=JobFunctions
        fields='__all__'

class JobIndustriesSerializer(serializers.ModelSerializer):   
    class Meta:
        model=JobIndustries
        fields='__all__'

class JobLocationSerializer(serializers.ModelSerializer):   
    class Meta:
        model=JobLocation
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    Job_Function = JobFunctionSerializer()
    Job_Industries = JobIndustriesSerializer()
    Job_Location = JobLocationSerializer()
    job_details=JobDetailsSerializer(many=True)

    class Meta:
        model = Jobs
        fields = ['id', 'job_title', 'scraped_date','job_link', 'Job_Function', 'Job_Industries', 'Job_Location', 'job_details']
