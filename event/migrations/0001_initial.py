# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
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
            ],
        ),
        migrations.CreateModel(
            name='EventOrganizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=60)),
                ('address', models.TextField()),
                ('user', models.ForeignKey(to='account.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='EventRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rate', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Showtime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('event', models.OneToOneField(primary_key=True, serialize=False, to='event.Event')),
                ('group_name', models.CharField(unique=True, max_length=40)),
                ('vocalist', models.CharField(max_length=30, null=True)),
                ('musicians', models.TimeField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('event', models.OneToOneField(primary_key=True, serialize=False, to='event.Event')),
                ('director', models.CharField(max_length=40)),
                ('actors', models.CharField(max_length=1000)),
                ('year', models.PositiveSmallIntegerField()),
                ('story_summary', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('event', models.OneToOneField(primary_key=True, serialize=False, to='event.Event')),
                ('country1', models.CharField(max_length=30)),
                ('country2', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='showtime',
            name='event',
            field=models.ForeignKey(to='event.Event'),
        ),
        migrations.AddField(
            model_name='eventrating',
            name='event',
            field=models.ForeignKey(to='event.Event'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_organizer',
            field=models.ForeignKey(to='event.EventOrganizer'),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([('title', 'event_organizer', 'address')]),
        ),
    ]
