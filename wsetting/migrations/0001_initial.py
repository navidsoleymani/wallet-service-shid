# Generated by Django 3.1.4 on 2021-01-07 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaxMiN',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maximum', models.FloatField(default=1000000)),
                ('minimum', models.FloatField(default=1000)),
            ],
        ),
    ]
