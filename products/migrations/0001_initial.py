# Generated by Django 2.2.6 on 2019-11-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('cost', models.IntegerField(blank=True, default=50)),
                ('details', models.TextField()),
                ('rating', models.FloatField(blank=True)),
                ('seller', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank='True', upload_to='')),
                ('items_remaining', models.IntegerField(blank=True, default=50)),
            ],
        ),
    ]
