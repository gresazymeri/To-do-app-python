# Generated by Django 4.0.4 on 2023-02-21 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitgym', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='user_id',
        ),
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
