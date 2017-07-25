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
from django.conf.urls import url
from sql_review.views import review, StepView, instance_by_ajax_and_id, submitted_list

urlpatterns = [
    url(r'^review_result/(?P<record_id>[0-9]+)/', review, name='sql_review_review_result'),
    url(r'^step/', StepView.as_view(), name='sql_review_step'),
    url(r'^review_list/', StepView.as_view(), name='sql_review_step'),
    url(r'^instance_by_ajax_and_id/', instance_by_ajax_and_id, name='instance_by_ajax_and_id'),
    url(r'^submitted_list/', submitted_list, name='sql_review_submitted_list'),
]
