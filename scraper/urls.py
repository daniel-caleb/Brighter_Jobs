from django.urls import path, include
from .views import JobViewSet, JobDetailViewSet, JobFunctionViewset, JobLocationViewset, JobIndustriesViewset
from rest_framework import routers


rt = routers.DefaultRouter()
rt.register(r'BrighterMondayJobs', JobViewSet, basename='brighter')
rt.register(r'job_details', JobDetailViewSet)
rt.register(r'job_functions', JobFunctionViewset)
rt.register(r'job_locations', JobLocationViewset)
rt.register(r'job_industries', JobIndustriesViewset)

urlpatterns = [
    path('', include(rt.urls)),
    # path('api/accounts/' , include('accounts.urls'))
]