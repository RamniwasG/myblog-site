# Generated by Django 4.1.1 on 2022-09-19 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auther_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='auther',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.auther'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
