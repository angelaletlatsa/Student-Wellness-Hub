# Generated by Django 5.2 on 2025-04-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_moodentry_delete_moodtracker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='note',
            field=models.TextField(blank=True, default='neutral'),
            preserve_default=False,
        ),
    ]
