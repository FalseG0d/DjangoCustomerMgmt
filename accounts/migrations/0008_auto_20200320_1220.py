# Generated by Django 3.0.4 on 2020-03-20 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200320_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 27, 12, 20, 5, 413093)),
        ),
    ]
