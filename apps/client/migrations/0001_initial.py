# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number_card', models.IntegerField()),
                ('type_card', models.CharField(choices=[('MC', 'MasterCard'), ('VS', 'Visa'), ('DN', 'Dinner'), ('AE', 'American Express')], max_length=1)),
                ('security_number', models.IntegerField()),
                ('exp_date', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Cards',
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mail', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='card',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client'),
        ),
    ]