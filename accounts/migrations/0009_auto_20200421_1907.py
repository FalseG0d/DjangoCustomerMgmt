# Generated by Django 2.0 on 2020-04-21 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200421_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 19, 7, 18, 897268)),
        ),
    ]