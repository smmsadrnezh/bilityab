# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('account', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('plan_name', models.CharField(unique=True, max_length=30)),
                ('discount', models.PositiveSmallIntegerField()),
                ('remaining', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TicketPromotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('issued_time', models.DateTimeField()),
                ('event', models.ForeignKey(to='event.Event')),
                ('promotion', models.ForeignKey(to='promotion.Promotion')),
                ('user', models.ForeignKey(to='account.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='ticketpromotion',
            unique_together=set([('promotion', 'user', 'event')]),
        ),
    ]
