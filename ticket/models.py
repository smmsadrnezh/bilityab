from django.db import models

from account.models import CustomUser
from event.models import Event, Showtime


class PurchasedTicket(models.Model):
    showtime = models.ForeignKey(Showtime)
    user = models.ForeignKey(CustomUser)
    quantity = models.PositiveSmallIntegerField()
    purchased_date = models.DateTimeField()
    price = models.FloatField()
    receipt = models.CharField(max_length=50)

    class Meta:
        unique_together = (("showtime", "user", "purchased_date"),)


class TicketPosition(models.Model):
    ticket = models.ForeignKey(PurchasedTicket)
    section = models.PositiveIntegerField()
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()
