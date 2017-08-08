# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views import View
from forms import LoginForm


from models import UserProfile


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        data = {

        }
        return render(request, "users/login.html", data)

    def post(self, request):
        login_form = LoginForm(request.POST)
        username = request.POST.get("username", "")
        password = request.POST.get('password', "")
        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('statistics_topology'))
                else:
                    data = {
                        'msg': u'用户未激活'
                    }
                    return render(request, "users/login.html", data)
            else:
                data = {
                    "msg": u'用户名或密码错误',
                    "username": username,
                    "password": password,
                }
                return render(request, "users/login.html", data)
        else:
            data = {
                "username": username,
                "password": password,
                "login_form": login_form
            }
            return render(request, "users/login.html", data)
