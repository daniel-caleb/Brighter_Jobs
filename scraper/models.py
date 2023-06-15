from django.db import models

# Create your models here.
from django.db import models


class JobFunctions(models.Model):
    jobFunction = models.TextField(max_length=100)

class Jobs(models.Model):
    job_title =models.CharField(max_length=1000)
    scraped_date = models.CharField(max_length=1000)
    job_link = models.URLField(max_length=5000)

    Job_Function=models.ForeignKey(JobFunctions, related_name='Job_Functions', on_delete=models.CASCADE)

def __str__(self):
    return self.scraped_date
