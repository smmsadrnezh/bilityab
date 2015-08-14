# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_recoverrequests'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoveryRequests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('random_num', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to='account.CustomUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='recoverrequests',
            name='user',
        ),
        migrations.DeleteModel(
            name='RecoverRequests',
        ),
    ]
