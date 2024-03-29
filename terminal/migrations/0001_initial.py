# Generated by Django 4.2.5 on 2024-01-02 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModelTerminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('year_production', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stan',
            fields=[
                ('name', models.CharField(max_length=16, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, unique=True)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.modelterminal')),
                ('stan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.stan')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataStart', models.DateField()),
                ('dataEnd', models.DateField()),
                ('user', models.CharField(max_length=200)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.action')),
                ('terminal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terminal.terminal')),
            ],
        ),
    ]
