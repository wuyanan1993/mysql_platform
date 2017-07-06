from django import template

register = template.Library()


@register.filter(name='n2br')
def n2br(value):
    return value.replace('.', '</br>')
