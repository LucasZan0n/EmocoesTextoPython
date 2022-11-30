# Generated by Django 4.1.1 on 2022-11-29 05:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AnaliseSentimentos', '0006_alter_letra_usuario_alter_registro_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letra',
            name='sentimento',
            field=models.TextField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='letra',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registro',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]