# Generated by Django 3.1.5 on 2021-01-15 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpus', '0002_auto_20210113_2252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='Kelompok_id',
            new_name='kelompok_id',
        ),
    ]
