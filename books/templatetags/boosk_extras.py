from django import template
import datetime

register = template.Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter(name='to_lower')
def to_lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.simple_tag
def current_time():
    return datetime.datetime.now().isoformat()