# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0023_eventorganizer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionprice',
            name='event',
            field=models.ForeignKey(to='event.Event', related_name='position_prices'),
        ),
    ]
