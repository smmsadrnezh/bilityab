from django.db import models
from datetime import datetime
from account.models import CustomUser
from event.models import Event
from event.models import Showtime


class Promotion(models.Model):
    showtime = models.OneToOneField(Showtime)
    discount = models.PositiveSmallIntegerField()
    remaining = models.PositiveSmallIntegerField()
    issued_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "تخفیف"
        verbose_name_plural = "تخفیف ها"

    def __str__(self):
        return "%s" % self.showtime
