# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0013_auto_20150802_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.OneToOneField(primary_key=True, serialize=False, to='event.Event'),
        ),
    ]
