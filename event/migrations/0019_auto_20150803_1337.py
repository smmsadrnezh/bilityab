# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0018_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='producer',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='writers',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
