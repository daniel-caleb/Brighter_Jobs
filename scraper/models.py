from django.db import models

# Create your models here.
from django.db import models


class Jobs(models.Model):
    job_title =models.CharField(max_length=1000)
    scraped_date = models.CharField(max_length=1000)
    job_link = models.URLField(max_length=5000)

def __str__(self):
    return self.scraped_date
