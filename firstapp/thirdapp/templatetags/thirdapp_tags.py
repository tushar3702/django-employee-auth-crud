import datetime
from django import template

register = template.Library()

@register.simple_tag(name="today")
# @register.simple_tag
def get_date():
    return datetime.datetime.now()

@register.filter
def texts(value):
    return '"' + str(value) + '"'