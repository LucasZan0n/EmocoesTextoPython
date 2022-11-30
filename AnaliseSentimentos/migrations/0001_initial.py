# Generated by Django 4.1.1 on 2022-11-30 04:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=100)),
                ('password1', models.CharField(max_length=150)),
                ('password2', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Letra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeM', models.CharField(max_length=150, verbose_name='')),
                ('letra', models.TextField(max_length=10000, unique=True, verbose_name='')),
                ('sentimento', models.TextField(max_length=100000)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
