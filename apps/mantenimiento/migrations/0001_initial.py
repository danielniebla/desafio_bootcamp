# Generated by Django 4.1.2 on 2022-10-13 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.PositiveSmallIntegerField(verbose_name='Kilometraje')),
                ('description', models.CharField(max_length=320)),
                ('cost', models.PositiveSmallIntegerField(verbose_name='Costo')),
                ('date', models.DateField(verbose_name='Fecha de llegada')),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto.auto')),
            ],
        ),
    ]
