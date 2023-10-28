# Generated by Django 4.2.6 on 2023-10-28 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_auto_20231021_1353'),
        ('reviewmodul', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JumlahReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.PositiveIntegerField(default=0)),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='booklist.buku')),
            ],
        ),
    ]
