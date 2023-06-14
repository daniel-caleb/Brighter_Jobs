from django.db import models

# Create your models here.
from django.db import models


class JbDate(models.Model):
    job_title =models.CharField(max_length=1000)
    scraped_date = models.CharField(max_length=1000)
    job_image = models.URLField(max_length=5000)
    job_link = models.URLField(max_length=5000, default='')
    job_function = models.CharField(max_length=1000, default='')


def __str__(self):
    return self.scraped_date
