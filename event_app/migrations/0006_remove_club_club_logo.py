# Generated by Django 4.2.7 on 2023-12-08 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0005_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='club_logo',
        ),
    ]