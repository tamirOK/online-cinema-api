# Generated by Django 2.0.5 on 2018-05-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20180517_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='released_date',
            field=models.DateField(),
        ),
    ]