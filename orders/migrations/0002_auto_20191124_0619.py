# Generated by Django 2.2.6 on 2019-11-24 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='cost',
            field=models.IntegerField(null=True),
        ),
    ]
