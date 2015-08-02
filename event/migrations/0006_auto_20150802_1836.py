# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        ('event', '0005_auto_20150730_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='country1',
            new_name='away_team',
        ),
        migrations.RenameField(
            model_name='sport',
            old_name='country2',
            new_name='home_team',
        ),
        migrations.AddField(
            model_name='event',
            name='photo',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='eventrating',
            name='user',
            field=models.ForeignKey(default=1, to='account.CustomUser'),
        ),
        migrations.AlterField(
            model_name='sport',
            name='event',
            field=models.OneToOneField(serialize=False, related_name='teams', primary_key=True, to='event.Event'),
        ),
    ]
