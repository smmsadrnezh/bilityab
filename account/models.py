from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    balance = models.FloatField(default=0, verbose_name="موجودی حساب")
    is_organizer = models.BooleanField(default=0, verbose_name="برگزارکننده")
    gender = models.BooleanField(default=0, verbose_name="جنسیت")
    phone = models.IntegerField(default="02188888888", verbose_name="شماره تلفن")
    birth_date = models.DateField(verbose_name="تاریخ تولد")

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class RecoveryRequests(models.Model):
    user = models.OneToOneField(CustomUser, verbose_name="کاربر")
    random_num = models.CharField(max_length=30, verbose_name="عدد تصادفی")

    class Meta:
        verbose_name = "درخواست بازیابی"
        verbose_name_plural = "درخواست های بازیابی"

    def __str__(self):
        return str(self.user) + ': ' + self.random_num