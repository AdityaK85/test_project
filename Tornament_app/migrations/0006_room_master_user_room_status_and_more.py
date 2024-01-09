# Generated by Django 4.1.4 on 2024-01-07 17:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tornament_app', '0005_joinroom_created_dt_alter_room_master_created_dt_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_master',
            name='user_room_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='joinroom',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 22, 30, 33, 341101), null=True),
        ),
        migrations.AlterField(
            model_name='room_master',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 22, 30, 33, 341101), null=True),
        ),
        migrations.AlterField(
            model_name='room_master',
            name='tornament_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 22, 30, 33, 341101), null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='created_dt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 1, 7, 22, 30, 33, 341101), null=True),
        ),
    ]
