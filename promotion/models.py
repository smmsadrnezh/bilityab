from django.db import models
from account.models import CustomUser
from event.models import Event
# Create your models here.


class Promotion(models.Model):
    plan_name = models.CharField(unique=True, max_length=30)
    discount = models.PositiveSmallIntegerField()
    remaining = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s" % self.plan_name


class TicketPromotion(models.Model):
    promotion = models.ForeignKey(Promotion)
    user = models.ForeignKey(CustomUser)
    event = models.ForeignKey(Event)
    issued_time = models.DateTimeField()

    class Meta:
        unique_together = (("promotion", "user", "event"),)

    def __str__(self):
        return "promotion: %d \n event: %d" % (self.remaining, self.discount)