# Generated by Django 5.0.4 on 2024-05-27 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_schulsozialarbeit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schulsozialarbeit',
            name='telefon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
