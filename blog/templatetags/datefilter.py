from django import template

from khayyam import JalaliDatetime


register = template.Library()


@register.filter(name='khayyam')
def khayyam_filter(value):
    return JalaliDatetime(value).strftime('%d %B %Y')


@register.filter(name='date_format')
def strftime_filter(value):
    return value.strftime('%d %b %y')
