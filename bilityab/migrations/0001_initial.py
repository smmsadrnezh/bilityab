# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('text', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CommentEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='bilityab.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='CommentEventOrganizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='bilityab.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group_name', models.CharField(unique=True, max_length=40)),
                ('vocalist', models.CharField(max_length=30, null=True)),
                ('musicians', models.TimeField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to=settings.AUTH_USER_MODEL)),
                ('registration_date', models.DateField()),
                ('balance', models.FloatField()),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                (b'objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=90)),
                ('description', models.CharField(max_length=300, null=True)),
                ('type', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=50)),
                ('capacity', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=300)),
                ('price', models.FloatField(default=0)),
                ('photo', models.ImageField(default=b'default.jpg', null=True, upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=60)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.PositiveSmallIntegerField()),
                ('event', models.ForeignKey(to='bilityab.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('director', models.CharField(max_length=40)),
                ('actors', models.CharField(max_length=1000)),
                ('year', models.PositiveSmallIntegerField()),
                ('story_summary', models.CharField(max_length=300)),
                ('event', models.ForeignKey(to='bilityab.Event', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_name', models.CharField(unique=True, max_length=30)),
                ('discount', models.PositiveSmallIntegerField()),
                ('remaining', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchasedTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('purchased_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('event', models.ForeignKey(to='bilityab.Event')),
                ('user', models.ForeignKey(to='bilityab.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(related_name='+', to='bilityab.Comment')),
                ('reply_to', models.ForeignKey(related_name='+', to='bilityab.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('event', models.ForeignKey(to='bilityab.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country1', models.CharField(max_length=30)),
                ('country2', models.CharField(max_length=30)),
                ('event', models.ForeignKey(to='bilityab.Event', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TicketPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.PositiveSmallIntegerField(null=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('ticket', models.ForeignKey(to='bilityab.PurchasedTicket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued_time', models.DateTimeField()),
                ('event', models.ForeignKey(to='bilityab.Event')),
                ('promotion', models.ForeignKey(to='bilityab.Promotion')),
                ('user', models.ForeignKey(to='bilityab.CustomUser')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_organizer',
            field=models.ForeignKey(to='bilityab.EventOrganizer'),
        ),
        migrations.AddField(
            model_name='concert',
            name='event',
            field=models.ForeignKey(to='bilityab.Event', unique=True),
        ),
        migrations.AddField(
            model_name='commenteventorganizer',
            name='event_organizer',
            field=models.ForeignKey(to='bilityab.EventOrganizer'),
        ),
        migrations.AddField(
            model_name='commentevent',
            name='event',
            field=models.ForeignKey(to='bilityab.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='bilityab.CustomUser'),
        ),
        migrations.AlterUniqueTogether(
            name='ticketpromotion',
            unique_together=set([('promotion', 'user', 'event')]),
        ),
        migrations.AlterUniqueTogether(
            name='purchasedticket',
            unique_together=set([('event', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('title', 'event_organizer', 'address')]),
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('user', 'time')]),
        ),
    ]
