# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0003_auto_20160307_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='duration',
            field=models.IntegerField(default=None, help_text='Event Duration in minuets', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='end_time',
            field=models.DateTimeField(default=None, help_text='Event End Time', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quizmodel',
            name='start_time',
            field=models.DateTimeField(default=None, help_text='Event start Time', null=True),
            preserve_default=True,
        ),
    ]
