# Generated by Django 5.0.3 on 2024-03-15 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_connexionapp_desktop_app_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdeployment',
            name='app_server',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps_deployments', to='base.appserver'),
        ),
        migrations.AlterField(
            model_name='appdeployment',
            name='module_applicatif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apps_deployments', to='base.moduleapplicatif'),
        ),
    ]
