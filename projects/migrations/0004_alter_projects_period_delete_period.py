# Generated by Django 4.1.1 on 2022-09-20 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_period_remove_projects_languages_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='period',
            field=models.CharField(max_length=60),
        ),
        migrations.DeleteModel(
            name='Period',
        ),
    ]
