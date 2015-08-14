# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0029_showtime_organizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positionprice',
            name='from_column',
        ),
        migrations.RemoveField(
            model_name='positionprice',
            name='from_row',
        ),
        migrations.RemoveField(
            model_name='positionprice',
            name='to_column',
        ),
        migrations.RemoveField(
            model_name='positionprice',
            name='to_row',
        ),
        migrations.AddField(
            model_name='positionprice',
            name='organizer',
            field=models.ForeignKey(default=1, to='event.EventOrganizer'),
            preserve_default=False,
        ),
    ]
