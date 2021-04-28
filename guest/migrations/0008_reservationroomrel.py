# Generated by Django 3.2 on 2021-04-28 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '0007_delete_reservationroomrel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationRoomRel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.reservation')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='guest.room')),
            ],
            options={
                'unique_together': {('reservation_id', 'room_id')},
            },
        ),
    ]
