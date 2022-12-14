# Generated by Django 4.1.1 on 2022-09-20 17:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_remove_projects_languages_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('end_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='projects',
            name='languages',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='technologies',
        ),
        migrations.AddField(
            model_name='projects',
            name='languages',
            field=models.ManyToManyField(to='projects.programminglang'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='period',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects', to='projects.period'),
        ),
        migrations.AddField(
            model_name='projects',
            name='technologies',
            field=models.ManyToManyField(to='projects.technology'),
        ),
    ]
