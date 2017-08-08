# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
