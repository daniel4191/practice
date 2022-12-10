from django import template


# start code
register = template.Library()


@register.filter
def sub(value, arg):
    return value - arg
 