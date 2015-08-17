from django import template

from bilityab.change_date import ChangeDate


register = template.Library()


@register.filter(name='persian_date')
def cut(value, arg):
    if arg == 'without_week_day':
        return ChangeDate().get_persian_date(value)
    elif arg == 'date-time':
        return ChangeDate().get_persian_date_time(value)
    else:
        return ChangeDate().get_persian_date_week_day(value)
