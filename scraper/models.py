from django.db import models

# Create your models here.
from django.db import models


class JbDate(models.Model):
    job_title =models.CharField(max_length=1000)
    scraped_date = models.CharField(max_length=1000)
    job_image = models.CharField(max_length=1000)


def __str__(self):
    return self.scraped_date
