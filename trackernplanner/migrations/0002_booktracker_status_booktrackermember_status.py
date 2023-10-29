# Generated by Django 4.2.4 on 2023-10-28 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackernplanner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booktracker',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('finished', 'Finished')], default='in_progress', max_length=20),
        ),
        migrations.AddField(
            model_name='booktrackermember',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In Progress'), ('finished', 'Finished')], default='in_progress', max_length=20),
        ),
    ]
