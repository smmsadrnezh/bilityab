from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    balance = models.FloatField(default=0)
    is_organizer = models.BooleanField(default=0)
    gender = models.BooleanField(default=0)
    phone = models.IntegerField(default="02188888888")
    birth_date = models.DateField()

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()


class RecoveryRequests(models.Model):
    user = models.OneToOneField(CustomUser)
    random_num = models.CharField(max_length=30)

    class Meta:
        verbose_name = "درخواست بازیابی"
        verbose_name_plural = "درخواست های بازیابی"

    def __str__(self):
        return str(self.user) + ': ' + self.random_num