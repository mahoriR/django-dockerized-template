# Generated by Django 3.0.5 on 2020-05-19 11:52

import common.uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200518_0931'),
    ]

    operations = [
        migrations.AddField(
            model_name='platformuser',
            name='external_id',
            field=models.UUIDField(default=common.uuid.unique_uuid4, unique=True),
        ),
    ]
