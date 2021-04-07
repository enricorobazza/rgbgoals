# Generated by Django 3.2 on 2021-04-07 17:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_alter_goalhistory_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='areapermission',
            unique_together={('area', 'user')},
        ),
        migrations.AlterUniqueTogether(
            name='goalpermission',
            unique_together={('goal', 'user')},
        ),
    ]
