"""mysql_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from statistics.views import index, get_info, InstanceListView, topology, ProcessListView

urlpatterns = [
    url(r'^index/', index, name='statistics_index'),
    url(r'^get_info/', get_info, name='statistics_get_info'),
    url(r'^instance_list/', InstanceListView.as_view(), name='statistics_instance_list'),
    url(r'^process_list/', ProcessListView.as_view(), name='statistics_process_list'),
    url(r'^topology/', topology, name='statistics_topology'),
]
