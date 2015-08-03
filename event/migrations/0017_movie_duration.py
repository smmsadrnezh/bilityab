# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0016_movie_cast'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='duration',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
