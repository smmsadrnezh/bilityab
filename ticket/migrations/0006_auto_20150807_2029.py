# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20150804_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketposition',
            name='section',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
