# Generated by Django 2.0.10 on 2019-01-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triangulacao',
            name='data',
            field=models.DateField(),
        ),
    ]
