# Generated by Django 4.0.3 on 2022-05-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0004_alter_flight_destination_alter_flight_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]