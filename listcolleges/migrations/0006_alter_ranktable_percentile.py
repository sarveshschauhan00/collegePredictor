# Generated by Django 4.0.6 on 2022-07-15 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listcolleges', '0005_alter_ranktable_percentile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranktable',
            name='percentile',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)]),
        ),
    ]
