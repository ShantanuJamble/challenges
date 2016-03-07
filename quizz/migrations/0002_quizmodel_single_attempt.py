# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='single_attempt',
            field=models.BooleanField(default=False, help_text='Only one chance to attempt the quiz', verbose_name='Random Order'),
            preserve_default=True,
        ),
    ]
