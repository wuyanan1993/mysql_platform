# -*- coding: utf-8 -*-


from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=3)
    password = forms.CharField(required=True, min_length=3)


class UserAddForm(forms.Form):
    username = forms.CharField(required=True, min_length=3)
    password = forms.CharField(required=True, min_length=6)
    name = forms.CharField(required=True)
    email = forms.CharField(required=True)
    identity = forms.CharField(required=True)
    mobile_phone = forms.IntegerField(required=True)
