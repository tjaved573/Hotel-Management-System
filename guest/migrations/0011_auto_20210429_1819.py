# Generated by Django 3.2 on 2021-04-29 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0010_auto_20210429_0514'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reservationroomrel',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='reservationroomrel',
            name='reservation',
        ),
        migrations.RemoveField(
            model_name='reservationroomrel',
            name='room',
        ),
        migrations.DeleteModel(
            name='FeatureRoomRel',
        ),
        migrations.DeleteModel(
            name='ReservationRoomRel',
        ),
    ]
