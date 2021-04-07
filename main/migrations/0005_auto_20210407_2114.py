# Generated by Django 3.2 on 2021-04-07 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210407_1754'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ['start_date', 'area', 'title'], 'verbose_name_plural': 'goals'},
        ),
        migrations.RemoveField(
            model_name='goal',
            name='due_date',
        ),
        migrations.AddField(
            model_name='goal',
            name='recurrency',
            field=models.IntegerField(choices=[('1', 'Diário'), ('7', 'Semanal'), ('15', 'Quinzenal'), ('30', 'Mensal'), ('120', 'Trimestral'), ('180', 'Semestral'), ('365', 'Anual')], default=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='goal',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
