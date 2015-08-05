# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0028_event_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='showtime',
            name='organizer',
            field=models.ForeignKey(related_name='show_times', to='event.EventOrganizer', default=0),
            preserve_default=False,
        ),
    ]
