# Generated by Django 4.1.2 on 2022-10-13 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('marca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marca.marca')),
            ],
        ),
    ]
