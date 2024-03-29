# Generated by Django 4.2.6 on 2023-10-28 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordernborrow', '0006_remove_borrowedhistory_borrowed'),
        ('reviewmodul', '0006_remove_reviewmember_gambar_buku'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewOnce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_review', models.BooleanField(default=False)),
                ('review_history', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ordernborrow.borrowedhistory')),
            ],
        ),
    ]
