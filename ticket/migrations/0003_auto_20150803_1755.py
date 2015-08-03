# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150803_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketposition',
            name='section',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
