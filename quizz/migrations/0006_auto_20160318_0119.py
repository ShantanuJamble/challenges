# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizz', '0005_quizmodel_participents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizmodel',
            old_name='participents',
            new_name='participants',
        ),
    ]
