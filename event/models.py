from django.db import models

from account.models import CustomUser


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
    # photo = models.FilePathField(null=True, default="default.jpg")

    class Meta:
        unique_together = (("title", "event_organizer", "address"),)
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"
    def __str__(self):
        return "%s" % self.title


class PositionPrice(models.Model):
    event = models.ForeignKey(Event)
    from_column = models.PositiveIntegerField()
    to_column = models.PositiveIntegerField()
    from_row = models.PositiveIntegerField()
    to_row = models.PositiveIntegerField()
    price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "قیمت ها"


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