# Generated by Django 4.2.7 on 2024-01-27 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event_app', '0013_rename_club_event_club1'),
    ]

    operations = [
        migrations.CreateModel(
            name='joinrequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('name_of_club', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='event_app.club')),
            ],
        ),
    ]
