# Generated by Django 2.0.1 on 2018-01-13 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
