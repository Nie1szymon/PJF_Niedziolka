# Generated by Django 4.2.5 on 2024-01-11 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terminal', '0005_event_timeend_event_timestart_alter_event_dataend'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Event',
            new_name='EventActual',
        ),
        migrations.CreateModel(
            name='EventHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataStart', models.DateField()),
                ('timeStart', models.TimeField(null=True)),
                ('dataEnd', models.DateField(null=True)),
                ('timeEnd', models.TimeField(null=True)),
                ('description', models.TextField(null=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.action')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.terminal')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
