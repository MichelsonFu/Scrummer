# Generated by Django 4.2.5 on 2023-10-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanban', '0021_rename_weekly_progress_sprintparticipation_daily_progress_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='expected_hours',
            field=models.IntegerField(default=0),
        ),
    ]
