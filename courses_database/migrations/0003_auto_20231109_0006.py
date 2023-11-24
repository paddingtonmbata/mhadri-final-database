# Generated by Django 3.2.19 on 2023-11-08 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_database', '0002_alter_country_country_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursedata',
            old_name='target_audience',
            new_name='numbers_since_2015',
        ),
        migrations.AddField(
            model_name='coursedata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
