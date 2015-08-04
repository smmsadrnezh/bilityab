# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20150803_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketposition',
            name='ticket',
            field=models.ForeignKey(to='ticket.PurchasedTicket', related_name='positions'),
        ),
    ]
