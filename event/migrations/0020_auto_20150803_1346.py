# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0019_auto_20150803_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrating',
            name='event',
            field=models.ForeignKey(related_name='rates', to='event.Event'),
        ),
    ]
