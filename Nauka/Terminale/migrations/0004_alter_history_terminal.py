# Generated by Django 4.2.8 on 2023-12-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Terminale', '0003_alter_history_stan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='terminal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Terminale.terminale'),
        ),
    ]
