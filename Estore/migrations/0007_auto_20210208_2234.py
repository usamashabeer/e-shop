# Generated by Django 3.1.6 on 2021-02-08 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0006_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
