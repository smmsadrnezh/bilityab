# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0024_auto_20150804_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_organizers',
            field=models.ManyToManyField(to='event.EventOrganizer', null=True),
        ),
    ]
