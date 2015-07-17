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
    title = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return "%s" % self.title


class Event(models.Model):
    type = models.CharField(max_length=30)
    category = models.CharField(max_length=40)
    title = models.CharField(max_length=80)
    date = models.DateTimeField()
    capacity = models.PositiveIntegerField()
    event_organizer = models.ForeignKey(EventOrganizer)
    address = models.CharField(max_length=300)

    class Meta:
        unique_together = (("title", "date", "address"),)

    def __str__(self):
        return "%s" % self.title


class EventRating(models.Model):
    rate = models.PositiveSmallIntegerField()
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%d" % (self.event, self.rate)


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


class PurchasedTicket(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(CustomUser)
    quantity = models.PositiveSmallIntegerField()
    purchased_date = models.DateTimeField()
    price = models.FloatField()

    class Meta:
        unique_together = (("event", "user"),)

    def __str__(self):
        return "%s -- purchased by %s" % (self.event, self.user)


class TicketPosition(models.Model):
    ticket = models.ForeignKey(PurchasedTicket)
    section = models.PositiveSmallIntegerField(null=True)
    row = models.PositiveSmallIntegerField()
    column = models.PositiveSmallIntegerField()

    def __str__(self):
        return "%s -- purchased by %s \n row: %s column: %s" % (self.event, self.user)


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

    class Meta:
        unique_together = (("promotion", "user", "event"),)

    def __str__(self):
        return "promotion: %d \n event: %d" % (self.remaining, self.discount)
