# Generated by Django 5.0.4 on 2024-05-27 20:58

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_kindertageseinrichtungen_telefon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schulsozialarbeit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('objectid', models.IntegerField(null=True)),
                ('traeger', models.CharField(max_length=255)),
                ('leistungen', models.CharField(max_length=255)),
                ('bezeichnung', models.CharField(blank=True, max_length=255, null=True)),
                ('kurzbezeichnung', models.CharField(blank=True, max_length=255, null=True)),
                ('strasse', models.CharField(max_length=255)),
                ('plz', models.CharField(max_length=10)),
                ('ort', models.CharField(max_length=255)),
                ('telefon', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fax', models.CharField(blank=True, max_length=20, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('coordinates', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
            ],
        ),
    ]
