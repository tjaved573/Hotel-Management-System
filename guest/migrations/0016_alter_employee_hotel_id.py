# Generated by Django 3.2 on 2021-05-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0015_auto_20210503_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hotel_id',
            field=models.IntegerField(null=True),
        ),
    ]
