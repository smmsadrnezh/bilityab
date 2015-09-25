from django.db import models

from account.models import CustomUser
from event.models import Event, Showtime


class PurchasedTicket(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='tickets')
    user = models.ForeignKey(CustomUser)
    quantity = models.PositiveSmallIntegerField()
    purchased_date = models.DateTimeField()
    price = models.FloatField()
    receipt = models.CharField(max_length=50)

    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط ها"
        unique_together = (("user", "purchased_date"),)

    def __str__(self):
        return "%s -- purchased by %s" % (self.showtime, self.user)


class TicketPosition(models.Model):
    ticket = models.ForeignKey(PurchasedTicket, related_name='positions')
    section = models.PositiveIntegerField(null=True, blank=True)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = "صندلی"
        verbose_name_plural = "صندلی ها"

    def __str__(self):
        return "row: %s column: %s" % (self.row, self.column)
