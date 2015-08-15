# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0033_auto_20150809_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('discount', models.PositiveSmallIntegerField()),
                ('remaining', models.PositiveSmallIntegerField()),
                ('issued_time', models.DateTimeField()),
                ('showtime', models.OneToOneField(to='event.Showtime')),
            ],
        ),
    ]
