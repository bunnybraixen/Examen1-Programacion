# Generated by Django 4.2.13 on 2024-06-24 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0015_alter_carro_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consola',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('activo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FormaPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('activo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('activo', models.IntegerField()),
            ],
        ),
    ]
