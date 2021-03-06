# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('questionaries', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='questionaries.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='survey',
            field=models.ForeignKey(to='tasks.Survey'),
        ),
        migrations.AlterUniqueTogether(
            name='survey',
            unique_together={('task', 'user')},
        ),
    ]
