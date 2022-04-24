# Generated by Django 4.0.3 on 2022-04-23 19:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timestamp', '0003_alter_timestamp_created_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timestamp',
            name='created_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 24, 0, 50, 38, 764478), null=True, verbose_name='datetime at which this object has been first created '),
        ),
        migrations.AlterField(
            model_name='timestamp',
            name='modified_on',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 4, 24, 0, 50, 38, 764478), null=True, verbose_name='datetime at which this object was modifed last time'),
        ),
    ]
