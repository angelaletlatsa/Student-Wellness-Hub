# Generated by Django 5.2 on 2025-04-04 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_appointment_created_at_alter_appointment_full_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='created_at',
        ),
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(default='booked', max_length=20),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='full_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
    ]
