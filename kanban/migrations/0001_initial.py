# Generated by Django 4.2.4 on 2023-09-07 09:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('priority', models.CharField(choices=[('LW', 'Low'), ('MD', 'Medium'), ('IP', 'Important'), ('UR', 'Urgent'), ('IU', 'Important and Urgent')], default='MD', max_length=2)),
                ('tag', models.CharField(choices=[("None",'None'),("FE", "Frontend"), ("BE", "Backend"), ("API", "API"), ("DB", "Database"), ("FR","Framework"),("T", "Testing"),("UIUX", "UI/UX")], default='MD', max_length=2)),
                ('status', models.CharField(choices=[('NS', 'Not Started'), ('IP', 'In Progress'), ('CP', 'Completed')], default='NS', max_length=2)),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kanban.board')),
            ],
        ),
    ]
