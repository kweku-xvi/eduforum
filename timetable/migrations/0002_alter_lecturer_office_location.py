# Generated by Django 4.2.1 on 2024-03-19 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='office_location',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
