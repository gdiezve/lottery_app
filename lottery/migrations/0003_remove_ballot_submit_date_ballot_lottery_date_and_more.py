# Generated by Django 4.2.4 on 2023-08-05 13:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lottery', '0002_alter_ballot_submit_date_alter_lottery_lottery_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ballot',
            name='submit_date',
        ),
        migrations.AddField(
            model_name='ballot',
            name='lottery_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 13, 24, 53, 759176, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lottery',
            name='lottery_date',
            field=models.DateField(default=datetime.datetime(2023, 8, 5, 13, 24, 53, 759860, tzinfo=datetime.timezone.utc)),
        ),
    ]
