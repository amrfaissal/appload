# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_app_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='app',
            name='pub_date',
        ),
    ]
