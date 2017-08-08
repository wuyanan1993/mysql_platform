# -*- coding: utf-8 -*-


from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True, min_length=6)
    password = forms.CharField(required=True, min_length=6)
