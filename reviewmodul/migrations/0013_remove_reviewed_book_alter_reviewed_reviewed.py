# Generated by Django 4.2.6 on 2023-10-29 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviewmodul', '0012_alter_reviewed_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewed',
            name='book',
        ),
        migrations.AlterField(
            model_name='reviewed',
            name='reviewed',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='reviewmodul.reviewmember'),
        ),
    ]
