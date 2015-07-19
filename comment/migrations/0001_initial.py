# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('text', models.TimeField()),
                ('user', models.ForeignKey(to='account.CustomUser')),
            ],
        ),
        migrations.CreateModel(
            name='CommentEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='comment.Comment')),
                ('event', models.ForeignKey(to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='CommentEventOrganizer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(to='comment.Comment')),
                ('event_organizer', models.ForeignKey(to='event.EventOrganizer')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.ForeignKey(related_name='+', to='comment.Comment')),
                ('reply_to', models.ForeignKey(related_name='+', to='comment.Comment')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='comment',
            unique_together=set([('user', 'time')]),
        ),
    ]
