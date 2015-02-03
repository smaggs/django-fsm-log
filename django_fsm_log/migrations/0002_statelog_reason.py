# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_fsm_log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statelog',
            name='reason',
            field=models.CharField(max_length=1024, null=True, blank=True),
            preserve_default=True,
        ),
    ]
