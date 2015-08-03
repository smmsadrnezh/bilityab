# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0021_eventorganizer_phone'),
        ('account', '0007_auto_20150803_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchasedTicket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('purchased_date', models.DateTimeField()),
                ('price', models.FloatField()),
                ('receipt', models.CharField(max_length=50)),
                ('event', models.OneToOneField(to='event.Showtime')),
                ('user', models.ForeignKey(to='account.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='TicketPosition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('section', models.PositiveSmallIntegerField(null=True)),
                ('row', models.PositiveSmallIntegerField()),
                ('column', models.PositiveSmallIntegerField()),
                ('ticket', models.ForeignKey(to='ticket.PurchasedTicket')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='purchasedticket',
            unique_together=set([('event', 'user')]),
        ),
    ]
