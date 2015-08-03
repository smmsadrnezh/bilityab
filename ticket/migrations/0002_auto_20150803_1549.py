# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchasedticket',
            old_name='event',
            new_name='showtime',
        ),
        migrations.AlterUniqueTogether(
            name='purchasedticket',
            unique_together=set([('showtime', 'user', 'purchased_date')]),
        ),
    ]
