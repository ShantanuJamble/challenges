# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0002_quizmodel_single_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizmodel',
            name='single_attempt',
            field=models.BooleanField(default=False, help_text='Only one chance to attempt the quiz', verbose_name='Single Attempt'),
            preserve_default=True,
        ),
    ]
