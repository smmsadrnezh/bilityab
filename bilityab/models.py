from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more. """

    registration_date = models.DateField()
    balance = models.FloatField()

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()


class EventOrganizer(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return "%s" % self.title


class Event(models.Model):
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    event_organizer = models.ForeignKey(EventOrganizer)
    address = models.TextField

    def __str__(self):
        return "%s" % self.title


class Comment(models.Model):
    user = models.ForeignKey(CustomUser)
    time = models.DateTimeField()
    text = models.TimeField()


class CommentEvent(models.Model):
    comment = models.ForeignKey(Comment)
    event = models.ForeignKey(Event)


class CommentEventOrganizer(models.Model):
    comment = models.ForeignKey(Comment)
    event_organizer = models.ForeignKey(EventOrganizer)


# class ReplyComment(models.Model):
#     comment = models.ForeignKey(Comment)
#     reply_to = models.ForeignKey(Comment)


class PurchasedTicket(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(CustomUser)
    quantity = models.PositiveSmallIntegerField()
    purchased_date = models.DateTimeField()
    price = models.FloatField()


class TicketPosition(models.Model):
    user = models.ForeignKey(CustomUser)
    event = models.ForeignKey(Event)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()


class Promotion(models.Model):
    plan_name = models.CharField(unique=True, max_length=20)
    discount = models.PositiveSmallIntegerField()
    remaining = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s" % self.plan_name


class TicketPromotion(models.Model):
    promotion = models.ForeignKey(Promotion)
    user = models.ForeignKey(CustomUser)
    event = models.ForeignKey(Event)
    issued_time = models.DateTimeField()

    def __str__(self):
        return "promotion: %s \n event: %s" % (self.remaining, self.discount)
