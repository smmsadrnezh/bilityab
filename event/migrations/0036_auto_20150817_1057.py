# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150814_2105'),
        ('event', '0035_auto_20150813_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserFavoriteEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to='account.CustomUser')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userfavoriteevents',
            unique_together=set([('user', 'event')]),
        ),
    ]
