# Generated by Django 4.2.6 on 2023-10-28 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewmodul', '0003_alter_jumlahreview_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumlahreview',
            name='jumlah',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
