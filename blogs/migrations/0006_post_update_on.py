# Generated by Django 4.1.1 on 2022-09-18 18:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_remove_post_update_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='update_on',
            field=models.CharField(default=datetime.date.today, max_length=50),
        ),
    ]
