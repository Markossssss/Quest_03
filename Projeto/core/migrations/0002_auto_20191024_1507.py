# Generated by Django 2.1.5 on 2019-10-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluguel',
            name='hora_inicio',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='aluguel',
            name='hora_termino',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
