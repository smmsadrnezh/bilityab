from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.


class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more. """

    registration_date = models.DateField()
    balance = models.FloatField()
    is_organizer = models.BooleanField(default=0)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()