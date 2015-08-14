# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('ticket', '0004_auto_20150803_2056'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='purchasedticket',
            unique_together=set([('user', 'purchased_date')]),
        ),
    ]
