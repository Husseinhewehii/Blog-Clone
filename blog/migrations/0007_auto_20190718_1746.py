# Generated by Django 2.2.1 on 2019-07-18 15:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190718_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 15, 46, 7, 946383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 18, 15, 46, 7, 945384, tzinfo=utc)),
        ),
    ]
