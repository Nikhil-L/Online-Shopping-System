# Generated by Django 2.2.6 on 2019-11-24 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191124_0619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='pincode',
            field=models.IntegerField(null=True),
        ),
    ]
