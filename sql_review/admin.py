# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sql_review.models import SqlReviewRecord

# Register your models here.


class SqlReviewRecordAdmin(admin.ModelAdmin):
    pass


admin.site.register(SqlReviewRecord, SqlReviewRecordAdmin)