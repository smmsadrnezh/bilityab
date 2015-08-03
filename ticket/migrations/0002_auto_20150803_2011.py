# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedticket',
            name='showtime',
            field=models.ForeignKey(to='event.Showtime'),
        ),
        migrations.AlterField(
            model_name='ticketposition',
            name='section',
            field=models.PositiveIntegerField(),
        ),
    ]
