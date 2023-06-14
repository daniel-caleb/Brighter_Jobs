from django.urls import path, include
from .views import JobViewSet
from rest_framework import routers


rt = routers.DefaultRouter()
rt.register(r'jobs', JobViewSet)

urlpatterns = [
    path('', include(rt.urls))
]