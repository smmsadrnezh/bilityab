from django import template
from bilityab.change_date import ChangeDate

register = template.Library()


@register.filter(name='persian_date')
def persian_date(value):
    return ChangeDate().get_persian_date(value)
