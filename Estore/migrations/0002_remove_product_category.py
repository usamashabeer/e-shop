# Generated by Django 3.1.6 on 2021-02-02 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
    ]
