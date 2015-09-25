from django.db import models

from account.models import CustomUser
from event.models import Event, Showtime


class PurchasedTicket(models.Model):
    showtime = models.ForeignKey(Showtime, related_name='tickets', verbose_name="سانس")
    user = models.ForeignKey(CustomUser, verbose_name="کاربر")
    quantity = models.PositiveSmallIntegerField(verbose_name="تعداد")
    purchased_date = models.DateTimeField(verbose_name="تاریخ خرید")
    price = models.FloatField(verbose_name="قیمت")
    receipt = models.CharField(max_length=50, verbose_name="شناسه خرید")

    class Meta:
        verbose_name = "بلیط"
        verbose_name_plural = "بلیط ها"
        unique_together = (("user", "purchased_date"),)

    def __str__(self):
        return "%s -- خریدار:  %s" % (self.showtime, self.user)


class TicketPosition(models.Model):
    ticket = models.ForeignKey(PurchasedTicket, related_name='positions', verbose_name="بلیط")
    section = models.PositiveIntegerField(null=True, blank=True, verbose_name="قسمت")
    row = models.PositiveSmallIntegerField(verbose_name="ردیف")
    column = models.PositiveSmallIntegerField(verbose_name="ستون")

    class Meta:
        verbose_name = "صندلی"
        verbose_name_plural = "صندلی ها"

    def __str__(self):
        return "ردیف: %s ستون: %s" % (self.row, self.column)
