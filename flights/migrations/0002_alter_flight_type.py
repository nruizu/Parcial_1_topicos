# Generated by Django 5.1.6 on 2025-02-26 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='type',
            field=models.CharField(choices=[('Domestic', 'Domestic'), ('International', 'International')], max_length=64),
        ),
    ]
