# Generated by Django 4.0.6 on 2022-07-14 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listcolleges', '0003_remove_ranktable_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ranktable',
            old_name='catagory_rank',
            new_name='main_catagory_rank',
        ),
    ]
