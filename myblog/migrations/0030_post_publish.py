# Generated by Django 4.0.2 on 2022-03-27 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0029_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 27, 23, 25, 49, 346050), null=True),
        ),
    ]
