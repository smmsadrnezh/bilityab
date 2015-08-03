# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150803_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='showtime',
            field=models.ForeignKey(to='event.Showtime', related_name='tickets'),
        ),
    ]
