from django.db import models

# Create your models here.
from django.db import models


class JobFunctions(models.Model):
    jobFunction = models.TextField(max_length=100)

class JobIndustries(models.Model):
    jobIndustries = models.TextField(max_length=100)

class JobLocation(models.Model):
    jobLocation = models.TextField(max_length=100)

class Jobs(models.Model):
    job_title =models.CharField(max_length=1000)
    scraped_date = models.CharField(max_length=1000)
    job_link = models.URLField(max_length=5000)

    Job_Function=models.ForeignKey(JobFunctions, related_name='Job_Functions', on_delete=models.CASCADE)
    Job_Industries=models.ForeignKey(JobIndustries, related_name='Job_Industries', on_delete=models.CASCADE)
    Job_Location=models.ForeignKey(JobLocation, related_name='Job_Location', on_delete=models.CASCADE)
    Job_Details = models.TextField(max_length=1000, default='')

def __str__(self):
    return self.scraped_date

class JobDetails(models.Model):
    job = models.ForeignKey(Jobs, related_name='job_details', on_delete=models.CASCADE)
    details=models.TextField(max_length=20000)
