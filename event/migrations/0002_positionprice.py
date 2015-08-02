# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionPrice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_column', models.PositiveIntegerField()),
                ('to_column', models.PositiveIntegerField()),
                ('from_row', models.PositiveIntegerField()),
                ('to_row', models.PositiveIntegerField()),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
    ]