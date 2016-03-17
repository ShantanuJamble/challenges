# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz', '0004_auto_20160313_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizmodel',
            name='participents',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True),
            preserve_default=True,
        ),
    ]
