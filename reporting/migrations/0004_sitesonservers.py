# Generated by Django 3.1.7 on 2021-03-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0003_grandprofitabilityreport'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitesOnServers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True, verbose_name='domain name')),
                ('name', models.CharField(max_length=50, verbose_name='display name')),
                ('from_server', models.IntegerField(default=0)),
                ('from_id', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'site',
                'verbose_name_plural': 'sites',
                'ordering': ('domain',),
            },
        ),
    ]
