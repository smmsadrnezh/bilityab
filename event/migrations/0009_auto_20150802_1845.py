# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0008_remove_sport_home_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.ForeignKey(serialize=False, related_name='teams', primary_key=True, to='event.Event'),
        ),
    ]
