# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quizz', '0005_quizmodel_participents'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSessions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(default=None, help_text='Participant End Time', null=True)),
                ('end_time', models.DateTimeField(default=None, help_text='Participant End Time', null=True)),
                ('quiz', models.OneToOneField(to='quizz.QuizModel')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
