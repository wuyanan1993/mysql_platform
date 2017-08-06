# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from statistics.models import MysqlInstanceGroup, MysqlInstance

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class SqlReviewRecord(models.Model):
    for_what = models.CharField(max_length=255, verbose_name=u'执行sql的目的')
    instance_group = models.ForeignKey(MysqlInstanceGroup, verbose_name=u'实例组', null=False, blank=False)
    instance = models.ForeignKey(MysqlInstance, verbose_name=u'对应组内的具体实例', null=False, blank=False)
    submit_time = models.DateTimeField(verbose_name=u'提交请求的时间', auto_now=True)
    execute_time = models.DateTimeField(verbose_name=u'要求执行的时间', null=False, blank=False)
    sql = models.TextField(verbose_name=u'想要执行的SQL', null=False, blank=False)
    is_checked = models.BooleanField(verbose_name=u'是否通过代码审核', default=0)
    is_submitted = models.BooleanField(verbose_name=u'是否提交至审核', default=0)
    is_reviewed = models.BooleanField(verbose_name=u'是否项目经理审核', default=0)
    is_executed = models.BooleanField(verbose_name=u'是否执行完成', default=0)

    def __str__(self):
        return self.for_what

    class Meta:
        verbose_name = u'SQL审核提交记录'
        verbose_name_plural = verbose_name


class SqlBackupRecord(models.Model):
    review_record_id = models.IntegerField(default=0, null=False, blank=False, verbose_name=u'对应审核记录的id')
    sequence = models.CharField(max_length=30, verbose_name=u'执行结果中的sequence，用来查找多用的回滚语句', default='',
                                null=False, blank=False)
    backup_db_name = models.CharField(max_length=40, default='', null=False, blank=False, verbose_name=u'备份数据库名')
    sql_sha1 = models.CharField(max_length=50, default='', null=True, blank=True, verbose_name=u'如果是osc，会有此值')


class SpecificationTypeForSql(models.Model):
    type = models.CharField(max_length=20, verbose_name=u'规范类型', null=False, blank=False, default=u'公共检查项')

    def __str__(self):
        return '{}'.format(self.type)

    class Meta:
        verbose_name = u'SQL规范类型'
        verbose_name_plural = verbose_name


class SpecificationContentForSql(models.Model):
    type = models.ForeignKey(SpecificationTypeForSql, null=False, blank=False)
    content = models.CharField(max_length=255, verbose_name=u'规范内容', null=False, blank=False, default=u'0')

    def __str__(self):
        return '{}--{}'.format(self.type, self.content)

    class Meta:
        verbose_name = u'SQL规范内容'
        verbose_name_plural = verbose_name