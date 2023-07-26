from django.contrib import admin
from .models import Jobs, JobDetails, JobFunctions, JobLocation, JobIndustries
# Register your models here.
admin.site.register(Jobs)
admin.site.register(JobDetails)
admin.site.register(JobFunctions)
admin.site.register(JobLocation)
admin.site.register(JobIndustries)