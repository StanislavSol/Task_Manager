# Generated by Django 4.2.6 on 2023-12-01 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0006_alter_status_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 1, 13, 26, 58, 417016, tzinfo=datetime.timezone.utc), verbose_name='date joined'),
        ),
    ]
