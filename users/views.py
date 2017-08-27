# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.shortcuts import render, redirect, reverse
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.views import View
from django.contrib.auth.decorators import login_required

from forms import LoginForm, UserAddForm
from utils.send_email import send_user_email

from models import UserProfile

from utils.log import my_logger


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
        if request.user.is_anonymous.value:
            data = {

            }
            return render(request, "users/login.html", data)
        else:
            # 以下代码会导致循环重定向
            # callback_url = request.GET.get('next')
            # if callback_url:
            #     return redirect(callback_url)
            # else:
            return redirect(reverse('statistics_topology'))

    def post(self, request):
        login_form = LoginForm(request.POST)
        username = request.POST.get("username", "")
        password = request.POST.get('password', "")
        if login_form.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    my_logger(level='info', message='登陆成功', username=request.user.name, path=request.path)
                    return redirect(reverse('statistics_topology'))
                else:
                    data = {
                        'msg': u'用户未激活',
                        "username": username,
                        "password": password,
                    }
                    my_logger(level='warning', message='未激活用户登陆尝试', username=username, path=request.path)
                    return render(request, "users/login.html", data)
            else:
                data = {
                    "msg": u'用户名或密码错误',
                    "username": username,
                    "password": password,
                }
                my_logger(level='warning', message='错误账号密码登陆尝试', username=username, path=request.path)
                return render(request, "users/login.html", data)
        else:
            data = {
                "msg": u'用户名或密码不符合规范',
                "username": username,
                "password": password,
                "login_form": login_form
            }
            return render(request, "users/login.html", data)


@login_required()
def my_logout(request):
    logout(request)
    data = {

    }
    return render(request, "users/login.html", data)


def test_email(request):
    send_user_email('173776778@qq.com', 'register')
    return HttpResponse('ok', status=200)


@login_required()
def user_add(request):
    data = {

    }
    return render(request, 'users/user_add.html', data)


@login_required(identity=('operation', ))
def deal_user_add(request):

    print(request.POST)
    user_add_form = UserAddForm(request.POST)
    if user_add_form.is_valid():

        user_obj = UserProfile()
        user_obj.username = user_add_form.cleaned_data.get('username')
        user_obj.password = make_password(user_add_form.cleaned_data.get('password'))
        user_obj.name = user_add_form.cleaned_data.get('name')
        user_obj.email = '{}{}'.format(user_add_form.cleaned_data.get('email'), '@voole.com')
        user_obj.identity = user_add_form.cleaned_data.get('identity')
        user_obj.mobile_phone = user_add_form.cleaned_data.get('mobile_phone')
        data = {
            'result_content': '用户添加成功，相关邮件已发送。'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        data = {
            'result_content': '填写内容校验失败，请检查。'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')