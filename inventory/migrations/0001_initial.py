# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-14 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagicItems',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=64, unique=True)),
                ('size_x', models.IntegerField()),
                ('size_y', models.IntegerField()),
            ],
            options={
                'db_table': 'magic_items',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MagicRuleIngredients',
            fields=[
                ('ingredient_id', models.AutoField(primary_key=True, serialize=False)),
                ('pos_x', models.IntegerField()),
                ('pos_y', models.IntegerField()),
            ],
            options={
                'db_table': 'magic_rule_ingredients',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MagicRules',
            fields=[
                ('rule_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'magic_rules',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wizards',
            fields=[
                ('wizard_id', models.AutoField(primary_key=True, serialize=False)),
                ('wizard_name', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'wizards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos_x', models.PositiveSmallIntegerField()),
                ('pos_y', models.PositiveSmallIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.MagicItems')),
                ('wizard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Wizards')),
            ],
        ),
    ]