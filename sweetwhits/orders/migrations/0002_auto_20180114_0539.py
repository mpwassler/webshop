# Generated by Django 2.0.1 on 2018-01-14 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_productimage'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OderItem',
            new_name='OrderItem',
        ),
    ]
