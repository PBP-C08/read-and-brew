# Generated by Django 4.2.6 on 2023-11-29 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordernborrow', '0009_auto_20231127_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
    ]
