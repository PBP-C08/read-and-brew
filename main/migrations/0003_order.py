# Generated by Django 4.2.6 on 2023-10-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_profile_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=255)),
                ('food_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('amount', models.PositiveIntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]