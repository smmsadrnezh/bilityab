# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0010_auto_20150802_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.OneToOneField(to='event.Event'),
        ),
    ]
