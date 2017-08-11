# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your views here.


class UserProfile(AbstractUser):
    IDENTITY_CHOICES = (
        ('developer', u'开发'),
        ('project_manager', u'项目经理'),
        ('operation', u'运维')
    )
    name = models.CharField(max_length=30, verbose_name=u'名字', default='None', null=False, blank=False)
    identity = models.CharField(max_length=15, verbose_name=u'身份', default='developer', choices=IDENTITY_CHOICES)
    email = models.EmailField(max_length=20, default='', verbose_name='email', null=False, blank=False)
    mobile_phone = models.CharField(max_length=11, verbose_name='mobile_phone', null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png")

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '<{}>--{}'.format(self.username, self.name)


class EmailVerifyRecord(models.Model):
    SEND_TYPE_CHOICE = (
        ('register', u'register'),
        ('forget', u'forget')
    )
    code = models.CharField(max_length=20, verbose_name=u'code')
    email = models.EmailField(max_length=50, verbose_name=u'email')
    send_type = models.CharField(max_length=10, choices=SEND_TYPE_CHOICE, default='forget')
    send_time = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)

    class Meta:
        verbose_name = u'Email验证码'
        verbose_name_plural = verbose_name