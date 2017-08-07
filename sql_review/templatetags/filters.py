# coding: utf8
from django import template

register = template.Library()


@register.filter(name='n2br')
def n2br(value):
    return value.replace('.', '</br>')


@register.filter(name='format_stage_status')
def format_stage_status(value):
    # trans stage status to chinese
    if value == 'Audit completed':
        return u'审核完成'
    elif value == '''Execute Successfully
Backup successfully''':
        return u'执行成功，备份成功'
    elif value == 'Execute Successfully':
        return u'执行成功'
    else:
        return 'none'
