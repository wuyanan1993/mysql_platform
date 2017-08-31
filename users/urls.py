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
from views import LoginView, my_logout, test_email, user_add, deal_user_add, messages, new_message_by_ajax
from views import clear_unread_message_by_ajax

urlpatterns = [
    url(r'^login/', LoginView.as_view(), name='users_login'),
    url(r'^logout/', my_logout, name='users_logout'),
    url(r'^test_email/', test_email, name='users_send_email'),
    url(r'^user_add/', user_add, name='users_user_add'),
    url(r'^deal_user_add/', deal_user_add, name='users_deal_user_add'),
    url(r'^messages/', messages, name='users_messages'),
    url(r'^new_message_by_ajax/', new_message_by_ajax, name='users_new_message_by_ajax'),
    url(r'^clear_unread_message_by_ajax/', clear_unread_message_by_ajax, name='users_clear_unread_message_by_ajax'),

]
