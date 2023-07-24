from django.shortcuts import render
from .models import Jobs, JobFunctions, JobIndustries, JobLocation, JobDetails, JobImages
from rest_framework import viewsets
from .serializers import JobSerializer, JobFunctionSerializer, JobIndustriesSerializer, JobLocationSerializer, JobDetailsSerializer, JobImagesSerializer
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests

link = 'https://www.brightermonday.co.ke/jobs'


page = requests.get(link)
if page.status_code == 200:
    soup = BeautifulSoup(page.content, 'html.parser')
            # DROPDOWN MENU STARTS HERE !!!
            # SELECTION FOR JOB FUNCTIONS
    select_functions = soup.find('select', class_="w-full h-10 pl-2 text-gray-500 rounded-md border border-gray-300 hover:border-gray-400 focus:border-gray-400 placeholder-gray-400 focus:placeholder-gray-900 mb-3 w-full md:mb-0 md:mr-3")
    options_functions = select_functions.find_all('options')
    for option in options_functions:
        functions = JobFunctions()
        functions.jobFunction=option.get_Text()
        functions.save()

            # SELECTION FOR JOB INDUSTRIES
    select_industries = soup.find('select', class_="w-full h-10 pl-2 text-gray-500 rounded-md border border-gray-300 hover:border-gray-400 focus:border-gray-400 placeholder-gray-400 focus:placeholder-gray-900 mb-3 w-full md:mb-0 md:mr-3")
    options_industries = select_industries.find_all('options')
    for option in options_industries:
        industries = JobIndustries()
        industries.jobIndustries=option.get_Text()
        industries.save()

            # SELECTION FOR JOB LOCAIONS
    select_functions = soup.find('select', class_="w-full h-10 pl-2 text-gray-500 rounded-md border border-gray-300 hover:border-gray-400 focus:border-gray-400 placeholder-gray-400 focus:placeholder-gray-900 mb-3 w-full md:mb-0 md:mr-3")
    options_locations = select_functions.find_all('options')
    for option in options_locations:
        location = JobLocation()
        location.jobLocation=option.get_Text()
        location.save()
        

            # BASIC INFO ---JOB TITLE, JOB LINK, JOB DATE
    divs = soup.find_all('div',class_="mx-5 md:mx-0 flex flex-wrap col-span-1 mb-5 bg-white rounded-lg border border-gray-300 hover:border-gray-400 focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-gray-500")
    for job in divs:
        save=Jobs()
        job_title = job.find('div',class_="flex items-center").find('p',class_='text-lg font-medium break-words text-link-500').get_text().strip()
        job_link = job.find('div', class_="flex items-center").find('a', class_='relative mb-3 text-lg font-medium break-words focus:outline-none metrics-apply-now text-link-500 text-loading-animate')['href']
        dates = job.find('div',class_="flex flex-row items-start items-center px-5 py-3 w-full border-t border-gray-300").find('p', class_='ml-auto text-sm font-normal text-gray-700 text-loading-animate').get_text().strip()
        job_image = job.find('img')
        if job_image:
            src = job_image.get('src')
        else:
            continue

        if dates is not None:
            save.scraped_date=dates    



        # /* Job Functions, Details and Summary 
        # /* ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ */
        job_response = requests.get(job_link)
        job_soup = BeautifulSoup(job_response .content, 'html.parser')

        
        Job_function_name = job_soup.find('div',class_='flex flex-wrap justify-start pt-5 pb-2 px-4 w-full border-b border-gray-300 md:flex-nowrap md:px-5').find('div',class_='w-full text-gray-500').find('h2',class_='text-sm font-normal').find('a').get_text(strip=True)
        job_search = job_soup.find('div', class_='mt-3')
        Job_location_name = job_search.find('a', class_="text-sm font-normal px-3 rounded bg-brand-secondary-50 mr-2 mb-3 inline-block").get_text(strip=True)
        industry_search = job_soup.find('div', class_='w-full text-gray-500')
        Job_industries_name = industry_search.find_all('div')[1].find('a', class_='text-sm font-normal px-3 rounded bg-brand-secondary-50 mr-2 mb-3 inline-block').get_text(strip=True)

        jobFunction, _ = JobFunctions.objects.get_or_create(jobFunction=Job_function_name)
        jobIndustries, _ = JobIndustries.objects.get_or_create(jobIndustries=Job_industries_name)
        jobLocation, _ = JobLocation.objects.get_or_create(jobLocation=Job_location_name)
        job_image = JobImages(jobImages=src)
        job_image.save()

        new_job = Jobs(
            job_title=job_title,
            scraped_date=dates,
            job_link =job_link,
            Job_Function = jobFunction,
            Job_Industries = jobIndustries,
            Job_Location = jobLocation,
            Job_Image = job_image
        )

        new_job.save()


            # HERE WE SCRAP THE JOB DETAILS NESTED IN THE JOB LINK !!!
        jb_summary = job_soup.find('div', class_='py-5 px-4 border-b border-gray-300 md:p-5')
        if jb_summary.find('h3').get_text():
            description=JobDetails()
            description.job=new_job
            description.details=jb_summary.find('h3').get_text()
            description.save()
        if jb_summary.find('p').get_text():
            descriptio=JobDetails()
            description.job=new_job
            description.details=jb_summary.find('p').get_text()
            description.save()
        qualification = jb_summary.find('ul')
        if qualification:
            qualifications = qualification.find_all('li')
            for requirements in qualifications:
                description = JobDetails()
                description.job = new_job
                description.details=requirements.get_text()
                description.save()

        job_info = job_soup.find('div', class_='text-sm text-gray-500')

        for info in job_info:
            bold_tag =info.find('b')
            content=info.get_text()
            if bold_tag:
                job_detail = JobDetails(job=new_job, details=content,bold=True)
            else:
                job_detail = JobDetails(job=new_job, details=content,bold=False)
            job_detail.save()

            next_info = info.find_next_sibling()
            if next_info and next_info.name == 'ul':
                ul = info.find_next_sibling('ul')
                if ul:
                    cont1 = ''
                    for li in ul.find_all('li'):
                        cont1 = li.text.strip()
                        content = cont1
                        job_detail1 = JobDetails(job=new_job, details=content)
                        job_detail1.save()


class JobDetailViewSet(viewsets.ModelViewSet):
    queryset=JobDetails.objects.all()
    serializer_class=JobDetailsSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobSerializer

class JobFunctionViewset(viewsets.ModelViewSet):
    queryset = JobFunctions.objects.all()
    serializer_class = JobFunctionSerializer

class JobIndustriesViewset(viewsets.ModelViewSet):
    queryset = JobIndustries.objects.all()
    serializer_class = JobIndustriesSerializer

class JobLocationViewset(viewsets.ModelViewSet):
    queryset = JobLocation.objects.all()
    serializer_class = JobLocationSerializer

class JobImageViewset(viewsets.ModelViewSet):
    queryset = JobImages.objects.all()
    serializer_class = JobImagesSerializer