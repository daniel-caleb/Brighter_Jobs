from rest_framework import serializers
from .models import Jobs, JobFunctions, JobLocation, JobIndustries, JobDetails, JobImages
from datetime import datetime, timedelta



from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'FirstName','LastName']



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

class JobImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=JobImages
        fields='__all__'

class JobSerializer(serializers.ModelSerializer):
    Job_Function = JobFunctionSerializer()
    Job_Industries = JobIndustriesSerializer()
    Job_Location = JobLocationSerializer()
    Job_Image = JobImagesSerializer()
    job_details=JobDetailsSerializer(many=True)

    class Meta:
        model = Jobs
        fields = ['id', 'job_title', 'scraped_date','job_link', 'Job_Function', 'Job_Industries', 'Job_Location','Job_Image', 'job_details']
