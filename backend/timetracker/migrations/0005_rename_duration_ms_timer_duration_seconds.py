# Generated by Django 5.0.2 on 2024-02-18 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetracker', '0004_rename_finished_at_timer_completed_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timer',
            old_name='duration_ms',
            new_name='duration_seconds',
        ),
    ]
