# Generated by Django 3.1.7 on 2021-05-10 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0007_auto_20210510_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='freshers',
            name='tech7',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='freshers',
            name='tech8',
            field=models.CharField(default='', max_length=15),
        ),
    ]
