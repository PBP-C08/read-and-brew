# Generated by Django 4.2.6 on 2023-10-28 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewmodul', '0005_reviewmember_gambar_buku'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewmember',
            name='gambar_buku',
        ),
    ]
