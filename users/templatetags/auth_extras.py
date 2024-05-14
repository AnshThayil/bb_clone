from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter(name='translate')
def translate(grade, format):
    font = ['3', '3+', '4', '4+', '5', '5+', '6A','6A+','6B', '6B+', '6C', '6C+', '7A', '7A+', '7B', '7B+', '7C', '7C+', '8A', '8A+']
    v = ['B', '0-', '0', '0+', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']

    if (format):
        return 'fb ' + font[int(grade)]
    else:
        return 'V' + v[int(grade)]
