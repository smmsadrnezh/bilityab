# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models

from account.models import CustomUser


class EventOrganizer(models.Model):
    title = models.CharField(max_length=60, unique=True, verbose_name="عنوان")
    address = models.TextField(verbose_name="آدرس")
    phone = models.IntegerField(default="02188888888", verbose_name="شماره تلفن")
    user = models.ForeignKey(CustomUser, verbose_name="کاربر")
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت")
    photo = models.ImageField(null=True, verbose_name="عکس")

    class Meta:
        verbose_name = "برگزارکننده"
        verbose_name_plural = "برگزارکنندگان"

    def __str__(self):
        return "%s" % self.title


class Categories(models.Model):
    title = models.CharField(max_length=90, verbose_name="عنوان")
    parent = models.ForeignKey('self', null=True, verbose_name="گروه پدر")

    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"

    def __str__(self):
        return "%s" % self.title


class Event(models.Model):
    title = models.CharField(max_length=90, unique=True, verbose_name="عنوان")
    description = models.CharField(max_length=300, null=True, verbose_name="توضیحات")
    category = models.ForeignKey(Categories, related_name='events', verbose_name="گروه")
    event_organizers = models.ManyToManyField(EventOrganizer, verbose_name="برگزارکنندگان")
    address = models.CharField(max_length=300, verbose_name="آدرس")
    landscape = models.ImageField(null=True, default="default.jpg", upload_to='/media/', verbose_name="عکس ۱")
    portrait = models.ImageField(null=True, default="default.jpg", upload_to='/media/', verbose_name="عکس ۲")
    created_at = models.DateTimeField(default=datetime.now, verbose_name="زمان ایجاد")

    class Meta:
        verbose_name = "رویداد"
        verbose_name_plural = "رویدادها"

    def __str__(self):
        return "%s" % self.title


class PositionPrice(models.Model):
    event = models.ForeignKey(Event, related_name='position_prices', verbose_name="رویداد")
    organizer = models.ForeignKey(EventOrganizer, verbose_name="برگزارکننده")
    price = models.IntegerField(default=0, verbose_name="قیمت")

    class Meta:
        verbose_name = "قیمت"
        verbose_name_plural = "قیمت ها"

    def __str__(self):
        return "%s - %s - %d هزار تومان" % (self.organizer.title, self.event.title, self.price)


class Showtime(models.Model):
    event = models.ForeignKey(Event, related_name='show_times', verbose_name="رویداد")
    organizer = models.ForeignKey(EventOrganizer, related_name='show_times', verbose_name="برگزارکننده")
    date = models.DateField(verbose_name="تاریخ")
    from_time = models.TimeField(verbose_name="از ساعت")
    to_time = models.TimeField(verbose_name="تا ساعت")
    capacity = models.PositiveIntegerField(verbose_name="ظرفیت")

    class Meta:
        verbose_name = "سانس"
        verbose_name_plural = "سانس ها"

    def __str__(self):
        return "%s از ساعت %s الی %s -- %s -- %s" % (self.date, self.from_time, self.to_time,
                                               self.event.title, self.organizer.title)


class Concert(models.Model):
    event = models.OneToOneField(Event, primary_key=True, verbose_name="رویداد")
    group_name = models.CharField(unique=True, max_length=40, verbose_name="نام گروه")
    vocalist = models.CharField(null=True, max_length=30, verbose_name="خواننده")
    musicians = models.CharField(max_length=1000, verbose_name="نوازندگان")

    class Meta:
        verbose_name = "کنسرت"
        verbose_name_plural = "کنسرت ها"

    def __str__(self):
        return "%s با خوانندگی %s" % (self.group_name, self.vocalist)


class Movie(models.Model):
    event = models.OneToOneField(Event, primary_key=True, verbose_name="رویداد")
    director = models.CharField(max_length=40, verbose_name="کارگردان")
    actors = models.CharField(max_length=1000, verbose_name="بازیگران")
    year = models.PositiveSmallIntegerField(verbose_name="سال تولید")
    story_summary = models.CharField(max_length=300, verbose_name="خلاصه داستان")
    cast = models.CharField(max_length=1000, verbose_name="عوامل")
    duration = models.PositiveIntegerField(verbose_name="مدت زمان")
    genre = models.CharField(max_length=50, verbose_name="ژانر")
    producer = models.CharField(max_length=100, verbose_name="تهیه کننده")
    writers = models.CharField(max_length=200, verbose_name="نویسندگان")

    class Meta:
        verbose_name = "فیلم"
        verbose_name_plural = "فیلم ها"

    def __str__(self):
        return "%s، کاری از %s، محصول %s" % (self.event.title, self.director, self.year)


class Sport(models.Model):
    event = models.OneToOneField(Event, primary_key=True, verbose_name="رویداد")
    home_team = models.CharField(max_length=30, verbose_name="تیم میزبان")
    away_team = models.CharField(max_length=30, verbose_name="تیم مهمان")

    class Meta:
        verbose_name = "ورزشی"
        verbose_name_plural = "ورزشی"

    def __str__(self):
        return "%s - %s" % (self.home_team, self.away_team)


class EventRating(models.Model):
    rate = models.FloatField(verbose_name="امتیاز")
    event = models.ForeignKey(Event, related_name='rates', verbose_name="رویداد")
    user = models.ForeignKey(CustomUser, default=1, verbose_name="کاربر")

    class Meta:
        verbose_name = "امتیاز"
        verbose_name_plural = "امتیازها"

    def __str__(self):
        return "%f به %s" % (self.rate, self.event.title)


class GalleryPhoto(models.Model):
    event = models.ForeignKey(Event, related_name='gallery_photos', verbose_name="رویداد")
    pic = models.ImageField(verbose_name="عکس")

    class Meta:
        verbose_name = "گالری"
        verbose_name_plural = "گالری"

    def __str__(self):
        return "%s" % self.event.title


class UserFavoriteEvents(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="کاربر")
    event = models.ForeignKey(Event, verbose_name="رویداد")

    class Meta:
        unique_together = (("user", "event"),)

    def __str__(self):
        return str(self.user) + ': ' + self.event
