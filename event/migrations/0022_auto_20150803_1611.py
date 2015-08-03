# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_eventorganizer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_organizers',
            field=models.ManyToManyField(to='event.EventOrganizer'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(unique=True, max_length=90),
        ),
        migrations.AlterUniqueTogether(
            name='event',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_organizer',
        ),
    ]
