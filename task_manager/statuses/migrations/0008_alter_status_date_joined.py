# Generated by Django 4.2.6 on 2023-12-01 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0007_alter_status_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
