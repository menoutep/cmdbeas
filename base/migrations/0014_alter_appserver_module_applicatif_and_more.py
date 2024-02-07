# Generated by Django 4.2.5 on 2024-01-23 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_api_module_applicatif_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appserver',
            name='module_applicatif',
            field=models.ManyToManyField(related_name='apps_servers', through='base.AppDeployment', to='base.moduleapplicatif'),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='ip_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clusters', to='base.ipadress'),
        ),
        migrations.AlterField(
            model_name='cluster',
            name='servers',
            field=models.ManyToManyField(related_name='clusters', through='base.DeploiementCluster', to='base.server'),
        ),
        migrations.AlterField(
            model_name='database',
            name='module_applicatifs',
            field=models.ManyToManyField(related_name='databases', through='base.ConnexionBD', to='base.moduleapplicatif'),
        ),
        migrations.AlterField(
            model_name='datamodel',
            name='data_dictionnary',
            field=models.ManyToManyField(related_name='datas_models', through='base.DataDictionnaryModel', to='base.datadictionnary'),
        ),
        migrations.AlterField(
            model_name='server',
            name='sys_stockage',
            field=models.ManyToManyField(related_name='servers', through='base.Partition', to='base.systemestockage'),
        ),
    ]