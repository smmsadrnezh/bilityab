from django.db import models
from datetime import datetime
from account.models import CustomUser
from event.models import Event
from event.models import Showtime


class Promotion(models.Model):
    showtime = models.OneToOneField(Showtime, verbose_name="سانس")
    discount = models.PositiveSmallIntegerField(verbose_name="تخفیف")
    remaining = models.PositiveSmallIntegerField(verbose_name="تعداد باقیمانده")
    issued_time = models.DateTimeField(default=datetime.now, verbose_name="زمان اعمال")

    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیف ها"

    def __str__(self):
        return "%s / %d درصد تخفیف" % (self.showtime, self.discount)
