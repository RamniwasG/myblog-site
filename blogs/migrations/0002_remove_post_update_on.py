# Generated by Django 4.1.1 on 2022-09-18 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='update_on',
        ),
    ]
