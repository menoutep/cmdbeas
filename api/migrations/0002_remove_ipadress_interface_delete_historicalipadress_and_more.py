# Generated by Django 4.2.5 on 2024-01-21 09:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ipadress',
            name='interface',
        ),
        migrations.DeleteModel(
            name='HistoricalIpAdress',
        ),
        migrations.DeleteModel(
            name='IpAdress',
        ),
    ]
