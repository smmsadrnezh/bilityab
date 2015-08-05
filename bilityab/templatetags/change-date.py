from django import template
from bilityab.change_date import ChangeDate

register = template.Library()


@register.filter(name='persian_date')
def cut(value):
    return ChangeDate().get_persian_date(value)
