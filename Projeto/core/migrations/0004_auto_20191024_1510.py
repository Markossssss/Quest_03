# Generated by Django 2.1.5 on 2019-10-24 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191024_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='valor_aluguel',
            field=models.CharField(choices=[('Moeda', 'Moeda'), ('Cedula', 'Cedula')], default='Moeda', max_length=7),
        ),
    ]
