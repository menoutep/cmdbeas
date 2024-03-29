# Generated by Django 4.2.5 on 2024-01-13 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_application_apptype_backupstrategie_cluster_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeploiementCluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.cluster')),
            ],
            options={
                'verbose_name': 'Deploiement cluster',
                'verbose_name_plural': 'Deploiements cluster',
            },
        ),
        migrations.CreateModel(
            name='Partition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Connexion serveur et système de stockage',
                'verbose_name_plural': 'Connexion serveurs et systèmes de stockages',
            },
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type_server', models.CharField(choices=[('virtuel', 'virtuel'), ('physique', 'physique')], default='physique', max_length=200)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('nb_processor', models.IntegerField()),
                ('v_processor', models.IntegerField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cluster', models.ManyToManyField(through='base.DeploiementCluster', to='base.cluster')),
                ('rack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.rack')),
                ('sys_stockage', models.ManyToManyField(through='base.Partition', to='base.systemestockage')),
            ],
            options={
                'verbose_name': 'Serveur ',
                'verbose_name_plural': 'Serveurs',
            },
        ),
        migrations.AddField(
            model_name='partition',
            name='serveur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.server'),
        ),
        migrations.AddField(
            model_name='partition',
            name='stockage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.systemestockage'),
        ),
        migrations.CreateModel(
            name='HistoricalServer',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('type_server', models.CharField(choices=[('virtuel', 'virtuel'), ('physique', 'physique')], default='physique', max_length=200)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('nb_processor', models.IntegerField()),
                ('v_processor', models.IntegerField()),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('rack', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.rack')),
            ],
            options={
                'verbose_name': 'historical Serveur ',
                'verbose_name_plural': 'historical Serveurs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalPartition',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('serveur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.server')),
                ('stockage', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.systemestockage')),
            ],
            options={
                'verbose_name': 'historical Connexion serveur et système de stockage',
                'verbose_name_plural': 'historical Connexion serveurs et systèmes de stockages',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalDeploiementCluster',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('updated', models.DateTimeField(blank=True, editable=False)),
                ('created', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.TextField(null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('cluster', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.cluster')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('serveur', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='base.server')),
            ],
            options={
                'verbose_name': 'historical Deploiement cluster',
                'verbose_name_plural': 'historical Deploiements cluster',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AddField(
            model_name='deploiementcluster',
            name='serveur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.server'),
        ),
    ]
