from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more. """

    balance = models.FloatField(default=0)
    is_organizer = models.BooleanField(default=0)
    gender = models.BooleanField(default=0)
    phone = models.IntegerField(default="02188888888")
    birth_date = models.DateField()

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()
