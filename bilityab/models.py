from django.db import models
from django.contrib.auth.models import User, UserManager


class CustomUser(User):
    """Consider that this class inherit django user class.
    user class fields:  username, email, password, is_staff, is_active, date_joined and much more. """

    registration_date = models.DateField()
    balance = models.FloatField()
    is_organizer = models.BooleanField(default=0)

    # Use UserManager to get the create_user method, etc.
    objects = UserManager()


class EventOrganizer(models.Model):
    title = models.CharField(max_length=60, unique=True)
    address = models.TextField()
    user = models.ForeignKey(CustomUser)

    def __str__(self):
        return "%s" % self.title


class Event(models.Model):
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=300, null=True)
    type = models.CharField(max_length=40)
    category = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()
    event_organizer = models.ForeignKey(EventOrganizer)
    address = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    # photo = models.ImageField(null=True, default="default.jpg")

    class Meta:
        unique_together = (("title", "event_organizer", "address"),)

    def __str__(self):
        return "%s" % self.title


class Showtime(models.Model):
    event = models.ForeignKey(Event)
    date = models.DateField()
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self):
        return "%s -> %s to %s" % (self.date, self.from_time, self.to_time)


class Concert(models.Model):
    event = models.OneToOneField(Event, primary_key=True)
    group_name = models.CharField(unique=True, max_length=40)
    vocalist = models.CharField(null=True, max_length=30)
    musicians = models.TimeField(max_length=1000)

    def __str__(self):
        return "%s -> %s" % (self.group_name, self.vocalist)


class Movie(models.Model):
    event = models.OneToOneField(Event, primary_key=True)
    director = models.CharField(max_length=40)
    actors = models.CharField(max_length=1000)
    year = models.PositiveSmallIntegerField()
    story_summary = models.CharField(max_length=300)

    def __str__(self):
        return "%s (%s) \n %s" % (self.director, self.year, self.story_summary)


class Sport(models.Model):
    event = models.OneToOneField(Event, primary_key=True)
    country1 = models.CharField(max_length=30)
    country2 = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.country1, self.country2)


class EventRating(models.Model):
    rate = models.PositiveSmallIntegerField()
    event = models.ForeignKey(Event)

    def __str__(self):
        return "%d" % self.rate


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
    receipt = models.CharField(max_length=50)

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