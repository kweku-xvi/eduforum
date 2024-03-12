# Generated by Django 4.2.1 on 2024-03-12 12:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('poster', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField(blank=True, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('maps_link', models.CharField(blank=True, max_length=255, null=True)),
                ('event_link', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
