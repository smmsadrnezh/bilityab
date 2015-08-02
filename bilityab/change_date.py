# -*- coding: utf-8 -*-

import math

from datetime import datetime


class ChangeDate(object):
    GREGORIAN_EPOCH = 1721425.5
    PERSIAN_EPOCH = 1948320.5
    PERSIAN_WEEKDAYS = ["یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج شنبه", "جمعه", "شنبه"]
    PERSIAN_MONTHS = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور', 'مهر', 'آبان',
                      'آذر', 'دی', 'بهمن', 'اسفند']

    def __init__(self):
        self.year = datetime.now().year
        self.month = datetime.now().month
        self.day = datetime.now().day

    def change(self, **kwargs):
        self.year = kwargs['year'] if kwargs.get('year', None) else self.year
        self.month = kwargs['month'] if kwargs.get('month', None) else self.month
        self.day = kwargs['day'] if kwargs.get('day', None) else self.day
        j = ChangeDate.gregorian_to_jd(self.year, self.month, self.day)
        result = ChangeDate.jd_to_persian(j)
        year = result[0]
        month = result[1]
        day = int(result[2])
        week_day = self.PERSIAN_WEEKDAYS[self.jwday(j)]
        return year, month, day, week_day

    @staticmethod
    def leap_gregorian(year):
        return ((year % 4) == 0) and (not (((year % 100) == 0) and ((year % 400) != 0)))

    @staticmethod
    def gregorian_to_jd(year, month, day):
        var_1 = (ChangeDate.GREGORIAN_EPOCH - 1) + (365 * (year - 1))
        var_2 = math.floor((year - 1) / 4) + (-math.floor((year - 1) / 100))
        var_3 = math.floor((year - 1) / 400) + math.floor((((367 * month) - 362) / 12))
        var_5 = 0 if month <= 2 else (-1 if ChangeDate.leap_gregorian(year) != 0 else -2)
        var_4 = day
        return var_1 + var_2 + var_3 + var_4 + var_5

    @staticmethod
    def persian_to_jd(year, month, day):
        epbase = year - (474 if (year >= 0) else 473)
        epyear = 474 + epbase % 2820
        var_1 = ((month - 1) * 31) if (month <= 7) else (((month - 1) * 30) + 6)
        var_2 = math.floor(epbase / 2820) * 1029983
        var_3 = math.floor(((epyear * 682) - 110) / 2816) + (epyear - 1) * 365
        return var_1 + var_2 + day + var_3 + (ChangeDate.PERSIAN_EPOCH - 1)

    @staticmethod
    def jd_to_persian(jd):
        jd = math.floor(jd) + 0.5
        depoch = jd - ChangeDate.persian_to_jd(475, 1, 1)
        cycle = math.floor(depoch / 1029983)
        cyear = depoch % 1029983
        if cyear == 1029982:
            ycycle = 2820
        else:
            aux1 = math.floor(cyear / 366)
            aux2 = cyear % 366
            ycycle = math.floor(((2134 * aux1) + (2816 * aux2) + 2815) / 1028522) + aux1 + 1
        year = ycycle + (2820 * cycle) + 474
        if year <= 0:
            year -= 1
        yday = (jd - ChangeDate.persian_to_jd(year, 1, 1)) + 1
        month = math.ceil(yday / 31) if (yday <= 186) else math.ceil((yday - 6) / 30)
        day = (jd - ChangeDate.persian_to_jd(year, month, 1)) + 1
        return year, month, day

    @staticmethod
    def jwday(a):
        return math.floor((a + 1.5)) % 7

    def get_persian_date_time(self, date_time):
        persian_date = self.change(year=date_time.year, month=date_time.month, day=date_time.day)
        time_arr = str(date_time.time()).split(':')
        time = time_arr[0] + ':' + time_arr[1] + ':' + str(int(float(time_arr[2])))
        return str(persian_date[2]) + ' ' + self.PERSIAN_MONTHS[persian_date[1] - 1] + ' ' + str(
            persian_date[0]) + ' ، ' + time

    def get_persian_date(self, date):
        persian_date = self.change(year=date.year, month=date.month, day=date.day)
        return str(persian_date[2]) + ' ' + self.PERSIAN_MONTHS[persian_date[1] - 1] + ' ' + str(persian_date[0])