# Generated by Django 4.2.6 on 2023-10-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewmodul', '0004_alter_jumlahreview_jumlah'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmember',
            name='gambar_buku',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
