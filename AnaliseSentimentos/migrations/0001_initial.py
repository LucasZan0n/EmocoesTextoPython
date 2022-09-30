# Generated by Django 4.1.1 on 2022-09-28 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('senha', models.CharField(max_length=150, verbose_name='Senha')),
            ],
        ),

        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('senha', models.CharField(max_length=150, verbose_name='Senha')),
                ('registro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AnaliseSentimentos.Registro')),
            ],
        ),
    ]
