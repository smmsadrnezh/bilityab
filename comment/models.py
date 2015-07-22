from django.db import models
# -*- coding: utf-8 -*-
from account.models import CustomUser
from event.models import Event, EventOrganizer


class Comment(models.Model):
    user = models.ForeignKey(CustomUser)
    time = models.DateTimeField()
    text = models.TimeField()


    class Meta:
        unique_together = (("user", "time"),)

    def __str__(self):
        return "%s -- %s" % (self.text, self.user)


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
