# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitting',
            name='end_time',
            field=models.DateTimeField(default=None, help_text='Participant End Time', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='sitting',
            name='start_time',
            field=models.DateTimeField(default=None, help_text='Participant Start Time', null=True),
            preserve_default=True,
        ),
    ]
