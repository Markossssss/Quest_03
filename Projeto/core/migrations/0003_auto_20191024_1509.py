# Generated by Django 2.1.5 on 2019-10-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20191024_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='valor_cobrado',
            field=models.CharField(choices=[('Moeda', 'Moeda'), ('Cedula', 'Cedula')], default='Moeda', max_length=7),
        ),
    ]
