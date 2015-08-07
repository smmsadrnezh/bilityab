# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime
from account.models import CustomUser


class EventOrganizer(models.Model):
    title = models.CharField(max_length=60, unique=True)
    address = models.TextField()
    phone = models.IntegerField(default="02188888888")
    user = models.ForeignKey(CustomUser)
    capacity = models.PositiveIntegerField()
    photo = models.ImageField(null=True)

    def __str__(self):
        return "%s" % self.title


class Categories(models.Model):
    title = models.CharField(max_length=90)
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return "%s" % self.title


class Event(models.Model):
    title = models.CharField(max_length=90, unique=True)
    description = models.CharField(max_length=300, null=True)
    category = models.ForeignKey(Categories, related_name='events')
    capacity = models.PositiveIntegerField()
    event_organizers = models.ManyToManyField(EventOrganizer)
    address = models.CharField(max_length=300)
    photo = models.ImageField(null=True, default="default.jpg")
    created_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"

    def __str__(self):
        return "%s" % self.title


class PositionPrice(models.Model):
    event = models.ForeignKey(Event, related_name='position_prices')
    organizer = models.ForeignKey(EventOrganizer)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name_plural = "قیمت ها"

    def __str__(self):
        return "%s - %s - %f" % (self.organizer.title, self.event.title, self.price)


class Showtime(models.Model):
    event = models.ForeignKey(Event, related_name='show_times')
    organizer = models.ForeignKey(EventOrganizer, related_name='show_times')
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
    cast = models.CharField(max_length=1000)
    duration = models.PositiveIntegerField()
    genre = models.CharField(max_length=50)
    producer = models.CharField(max_length=100)
    writers = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s) \n %s" % (self.director, self.year, self.story_summary)


class Sport(models.Model):
    event = models.OneToOneField(Event, primary_key=True)
    home_team = models.CharField(max_length=30)
    away_team = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.home_team, self.away_team)


class EventRating(models.Model):
    rate = models.FloatField()
    event = models.ForeignKey(Event, related_name='rates')
    user = models.ForeignKey(CustomUser, default=1)

    def __str__(self):
        return "%f" % self.rate


