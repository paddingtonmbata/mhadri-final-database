# Generated by Django 3.2.19 on 2023-11-08 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_database', '0003_auto_20231109_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedata',
            old_name='traings_faculty',
            new_name='trainings_faculty',
        ),
    ]
