# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='answers_set',
            field=models.CommaSeparatedIntegerField(default=None, max_length=1024, verbose_name="User's Answers", blank=True),
            preserve_default=True,
        ),
    ]
