# Generated by Django 4.2.5 on 2024-01-12 22:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('terminal', '0008_rename_eventactual_historyevent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventHistorys',
            new_name='ActualEvent',
        ),
    ]