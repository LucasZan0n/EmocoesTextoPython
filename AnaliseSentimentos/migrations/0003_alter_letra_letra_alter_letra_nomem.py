# Generated by Django 4.1.1 on 2022-10-03 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnaliseSentimentos', '0002_alter_letra_nomem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letra',
            name='letra',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='letra',
            name='nomeM',
            field=models.CharField(max_length=150),
        ),
    ]
