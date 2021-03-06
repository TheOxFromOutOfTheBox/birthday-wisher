# Generated by Django 2.2.12 on 2020-05-23 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birthday',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birth_date',
            field=models.DateField(help_text='Valid Format: YYYY-MM-DD', verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='wisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
