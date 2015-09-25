# -*- coding: utf-8 -*-
from django.db import models
from account.models import CustomUser
from bilityab.change_date import ChangeDate
from event.models import Event, EventOrganizer


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="کاربر")
    time = models.DateTimeField(verbose_name="زمان و تاریخ")
    text = models.CharField(max_length=300, verbose_name="متن نظر")

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"
        unique_together = (("user", "time"),)

    def __str__(self):
        return "%s در تاریخ %s" % (self.user, ChangeDate().get_persian_date_time(self.time))


class CommentEvent(models.Model):
    comment = models.ForeignKey(Comment)
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%s -- %s" % (self.comment, self.event)


class CommentEventOrganizer(models.Model):
    comment = models.ForeignKey(Comment)
    event_organizer = models.ForeignKey(EventOrganizer)

    def __str__(self):
        return "%s -- %s" % (self.comment, self.event_organizer)


class ReplyComment(models.Model):
    comment = models.ForeignKey(Comment, related_name='+')
    reply_to = models.ForeignKey(Comment, related_name='+')

    def __str__(self):
        return "%s -- %s" % (self.comment, self.reply_to)
