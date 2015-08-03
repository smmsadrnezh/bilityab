# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0014_auto_20150802_2126'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventorganizer',
            name='capacity',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='showtime',
            name='event',
            field=models.ForeignKey(related_name='show_times', to='event.Event'),
        ),
    ]
