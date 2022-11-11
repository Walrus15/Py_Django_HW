from django import template

register = template.Library()


@register.filter(name='even')
def even(value):
    if value % 7 == 0:
        return True
    else:
        return False



