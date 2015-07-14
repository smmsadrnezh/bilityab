from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    registration_date = models.DateField()
    balance = models.FloatField()
    is_admin = models.BooleanField()


class Event(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    capacity = models.IntegerField()
    event_organizer_id = models.ForeignKey(EventOrganizer)
    address = models.TextField

    def __str__(self):
        return "%s" % self.title


class EventOrganizer(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return "%s" % self.title


class CommentEventOrganizer(models.Model):
    comment_id = models.ForeignKey(Comment)
    event_organizer_id = models.ForeignKey(EventOrganizer)


class Comment(models.Model):
    user_id = models.ForeignKey(CustomUser)
    time = models.DateTimeField()
    text = models.TimeField()
    reply_id = models.ForeignKey(Comment)


class CommentEvent(models.Model):
    comment_id = models.ForeignKey(Comment)
    event_id = models.ForeignKey(Event)


class PurchasedTicket(models.Model):
    event_id = models.ForeignKey(Event)
    user_id = models.ForeignKey(CustomUser)
    quantity = models.IntegerField()
    purchased_date = models.DateTimeField()
    price = models.FloatField()


class TicketPosition(models.Model):
    user_id = models.ForeignKey(CustomUser)
    event_id = models.ForeignKey(Event)
    row = models.IntegerField()
    column = models.IntegerField()


class TicketPromotion(models.Model):
    promotion_id = models.ForeignKey(Promotion)
    user_id = models.ForeignKey(CustomUser)
    event_id = models.ForeignKey(Event)
    issued_time = models.DateTimeField()


class Promotion(models.Model):
    remaining = models.IntegerField()
    discount  = models.IntegerField()

