# Generated by Django 5.0.4 on 2024-05-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_jugendberufshilfen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schulen',
            name='bezugnr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
