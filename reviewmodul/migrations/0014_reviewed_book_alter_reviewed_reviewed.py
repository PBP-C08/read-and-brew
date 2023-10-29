# Generated by Django 4.2.6 on 2023-10-29 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booklist', '0002_auto_20231021_1353'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviewmodul', '0013_remove_reviewed_book_alter_reviewed_reviewed'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewed',
            name='book',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='booklist.buku'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reviewed',
            name='reviewed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
