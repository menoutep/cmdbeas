# Generated by Django 4.2.5 on 2024-01-24 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_appserver_module_applicatif_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverroom',
            name='datacenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='servers_rooms', to='base.datacenter'),
        ),
    ]