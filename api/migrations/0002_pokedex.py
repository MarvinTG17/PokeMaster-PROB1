# Generated by Django 4.1.6 on 2023-02-08 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokedex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region_id', models.IntegerField()),
                ('identifier', models.CharField(max_length=100)),
                ('is_main_series', models.IntegerField()),
            ],
        ),
    ]