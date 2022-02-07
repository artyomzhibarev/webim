from django import template

register = template.Library()


@register.filter
def is_number(value):
    return True if isinstance(value, int) else False
