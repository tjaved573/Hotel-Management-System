# Generated by Django 3.2 on 2021-04-29 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0009_feature_featureroomrel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureroomrel',
            name='feature_id',
            field=models.ForeignKey(db_column='feature_id', on_delete=django.db.models.deletion.CASCADE, to='guest.feature'),
        ),
        migrations.AlterField(
            model_name='featureroomrel',
            name='room_id',
            field=models.ForeignKey(db_column='room_id', on_delete=django.db.models.deletion.CASCADE, to='guest.room'),
        ),
    ]
