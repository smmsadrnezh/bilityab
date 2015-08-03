import re
from datetime import datetime

from account.models import CustomUser


class CheckRegistration(object):
    @staticmethod
    def check_first_name(first_name):
        if first_name:
            if not re.match('^[ A-Za-z0-9-@+_\u0600-\u06FF]+$', first_name):
                return 'invalid_first_name'
            return ''
        else:
            return 'empty_first_name'

    @staticmethod
    def check_last_name(last_name):
        if last_name:
            if not re.match('^[ A-Za-z0-9-@+_\u0600-\u06FF]+$', last_name):
                return 'invalid_last_name'
            return ''
        else:
            return 'empty_last_name'

    @staticmethod
    def check_date(date):
        if date:
            try:
                date = date.split('/')
                year, month, day = int(date[0]), int(date[1]), int(date[2])
                if year < 1000 or year > datetime.now().year:
                    return 'date'
                if month > 12 or month < 1:
                    return 'date'
                if day > 31 or day < 1:
                    return 'date'
                return ''
            except ValueError:
                return 'date'
        else:
            return 'date'

    @staticmethod
    def check_pass(password):
        if password:
            if len(password) < 5:
                return 'password'
            return ''
        else:
            return 'password'

    @staticmethod
    def check_email(email):
        if email:
            if not re.match(r'^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$', email):
                return 'invalid_email'
            if CustomUser.objects.filter(email=email).exists():
                return 'registered_email'
            return ''
        else:
            return 'invalid_email'
