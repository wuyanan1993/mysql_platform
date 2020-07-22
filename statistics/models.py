# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.


class MysqlInstanceGroup(models.Model):
    name = models.CharField(max_length=20, null=False, verbose_name=u'实例组')
    code = models.CharField(max_length=2, null=False, default='vo', verbose_name=u'组代号')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Mysql 实例组'
        verbose_name_plural = verbose_name


class MysqlInstance(models.Model):
    CHARACTER_CHOICES = (
        ('main', 'main'),
        ('subordinate', 'subordinate'),
    )
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name=u'实例名称')
    group = models.ForeignKey(MysqlInstanceGroup, verbose_name=u'实例组名称')
    ip = models.GenericIPAddressField(null=False, blank=False, verbose_name='IP')
    port = models.IntegerField(null=False, blank=False, default=3306, verbose_name=u'实例端口')
    login_instance_account = models.CharField(max_length=20, null=False, blank=False,
                                              default='db_platform', verbose_name=u'登陆实例账号')
    login_instance_password = models.CharField(max_length=20, null=False, blank=False, verbose_name=u'登陆实例密码')
    x_position = models.IntegerField(null=False, blank=False, default=0, verbose_name=u'拓扑图中的x轴')
    y_position = models.IntegerField(null=False, blank=False, default=0, verbose_name=u'拓扑图中的y轴')

    def __str__(self):
        return '{}--{}--{}'.format(self.name, self.id, self.group)

    class Meta:
        verbose_name = u'Mysql 实例'
        verbose_name_plural = verbose_name
        unique_together = ('ip', 'port')


class InstanceRelation(models.Model):
    main_instance = models.ForeignKey(MysqlInstance, related_name='main_instance_id',
                                        blank=False, verbose_name=u'主id')
    subordinate_instance = models.ForeignKey(MysqlInstance, related_name='subordinate_instance_id',
                                       blank=False, verbose_name=u'从id')
    belong_group = models.ForeignKey(MysqlInstanceGroup, blank=False, default=1, verbose_name=u'Mysql 组')

    def __str__(self):
        return '{} ==> {}  ({})'.format(self.main_instance, self.subordinate_instance, self.belong_group)

    class Meta:
        verbose_name = u'Mysql 主从关系'
        verbose_name_plural = verbose_name


class BackupInstance(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name=u'实例名称')
    ip = models.GenericIPAddressField(null=False, blank=False, verbose_name='IP')
    port = models.IntegerField(null=False, blank=False, default=22, verbose_name=u'实例ssh端口')
    login_instance_account = models.CharField(max_length=20, null=False, blank=False,
                                              default='root', verbose_name=u'登陆实例账号')
    login_instance_password = models.CharField(max_length=20, null=False, blank=False, verbose_name=u'登陆实例密码')

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = u'Mysql 备份实例'
        verbose_name_plural = verbose_name
        unique_together = ('ip', 'port')