# Generated by Django 4.0.3 on 2022-03-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0006_remove_glucose_glucose_glucose_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glucose',
            name='category',
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]