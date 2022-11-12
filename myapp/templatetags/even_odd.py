from django import template
import random
from string import ascii_uppercase
from random import choice


register = template.Library()


@register.filter(name='even')
def even(value):
    if value % 7 == 0:
        return True
    else:
        return False

@register.filter(name='rand_url')
def rand_url(value):
    value = random.choice(value)
    return value

@register.filter(name='rand_slug')
def rand_slug(values):
    a = random.randint(0, 100)
    b = ''.join(choice(ascii_uppercase.lower()) for i in range(4))
    c = (str(a) + '/') + b
    return c


