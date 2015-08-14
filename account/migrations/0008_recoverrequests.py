# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20150803_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoverRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('random_num', models.CharField(max_length=30)),
                ('user', models.OneToOneField(to='account.CustomUser')),
            ],
        ),
    ]
