# Generated by Django 3.2.9 on 2021-12-04 23:57

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_app', '0002_alter_property_list_associated_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='list_associated_properties',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(max_length=255), default=list, size=None),
        ),
    ]