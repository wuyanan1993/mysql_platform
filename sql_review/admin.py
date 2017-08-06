# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from sql_review.models import SqlReviewRecord, SpecificationTypeForSql, SpecificationContentForSql

# Register your models here.


class SqlReviewRecordAdmin(admin.ModelAdmin):
    pass


class SpecificationContentForSqlAdmin(admin.ModelAdmin):
    pass


class SpecificationTypeForSqlAdmin(admin.ModelAdmin):
    pass

admin.site.register(SqlReviewRecord, SqlReviewRecordAdmin)
admin.site.register(SpecificationContentForSql, SpecificationContentForSqlAdmin)
admin.site.register(SpecificationTypeForSql, SpecificationTypeForSqlAdmin)

