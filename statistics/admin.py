# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import MysqlInstance, InstanceRelation, MysqlInstanceGroup, BackupInstance

# Register your models here.


class MysqlInstanceAdmin(admin.ModelAdmin):
    pass


class InstanceRelationAdmin(admin.ModelAdmin):
    pass


class MysqlInstanceGroupAdmin(admin.ModelAdmin):
    pass


class BackupInstanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(MysqlInstance, MysqlInstanceAdmin)
admin.site.register(InstanceRelation, InstanceRelationAdmin)
admin.site.register(MysqlInstanceGroup, MysqlInstanceGroupAdmin)
admin.site.register(BackupInstance, BackupInstanceAdmin)
