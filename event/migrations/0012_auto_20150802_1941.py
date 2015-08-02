# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0011_auto_20150802_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sport',
            name='id',
        ),
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.OneToOneField(serialize=False, primary_key=True, to='event.Event'),
        ),
    ]
