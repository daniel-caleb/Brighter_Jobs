from django.shortcuts import render
from .models import JbDate
from rest_framework import viewsets
from .serializers import JobSerializer
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

link = 'https://www.brightermonday.co.ke/jobs'
response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')
divs = soup.find_all('div',class_="mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500")

for job in divs:
    save=JbDate()
    job_title = job.find('div',class_="flex items-center").find('p',class_='text-lg font-medium break-words text-link-500').get_text().strip()
    job_link = job.find('div', class_="flex items-center").find('a', class_='relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-link-500 text-loading-animate')['href']
    # job_function = job.find('div', class_="flex items-center").find('p', class_='text-sm text-gray-500 text-loading-animate inline-block').get_text().strip()
    # job_image = job.find('div', class_="flex justify-center items-center p-1 w-[100px] h-[100px] align-middle bg-white rounded-md border-2 border-gray-300").find('img', class_='w-full h-full object-contain transition-opacity duration-200 ease-in rounded')['href']
    dates = job.find('div',class_="flex flex-row items-start items-center px-5 py-3 w-full border-t border-gray-300").find('p', class_='ml-auto text-sm font-normal text-gray-700 text-loading-animate').get_text().strip()

    if dates is not None:
        save.scraped_date=dates

    # save.job_function=job_function
    # save.job_image=job_image
    save.job_link=job_link
    save.job_title=job_title
    save.save()
class JobViewSet(viewsets.ModelViewSet):
    queryset = JbDate.objects.all()
    serializer_class = JobSerializer