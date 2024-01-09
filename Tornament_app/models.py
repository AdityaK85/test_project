import datetime
from django.db import models

# Create your models here.


class UserDetails(models.Model):
    username = models.CharField( max_length=100 , blank=True, null=True)
    email = models.CharField( max_length=100 , blank=True, null=True)
    password = models.CharField( max_length=100 , blank=True, null=True)
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())


class Room_Master(models.Model):
    fk_user = models.ForeignKey(UserDetails, on_delete=models.CASCADE , blank=True, null=True  )
    title = models.CharField( max_length=100 , blank=True, null=True)
    discription = models.TextField( blank=True, null=True)
    thumbnail = models.FileField(upload_to='thumbnail/', blank=True, null=True)
    selected_game = models.CharField( max_length=100 , blank=True, null=True)
    room_member = models.CharField( max_length=100 , blank=True, null=True)
    tornament_dt =  models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())
    start_tm =  models.TimeField(blank=True , null= True)
    end_tm =  models.TimeField(blank=True , null= True)
    room_type = models.CharField( max_length=100 , blank=True, null=True)
    room_password = models.CharField( max_length=100 , blank=True, null=True)
    game_type = models.CharField( max_length=100 , blank=True, null=True)
    team_member = models.CharField( max_length=100 , blank=True, null=True)
    custom_team = models.CharField( max_length=100 , blank=True, null=True)
    room_joining = models.CharField( max_length=100 , blank=True, null=True)
    room_joining_fee = models.CharField( max_length=100 , blank=True, null=True)
    game_map = models.CharField( max_length=100 , blank=True, null=True)
    game_room_id = models.CharField( max_length=100 , blank=True, null=True)
    game_room_type = models.CharField( max_length=100 , blank=True, null=True)
    game_room_type_pwd = models.CharField( max_length=100 , blank=True, null=True)
    available_seats = models.CharField( max_length=100 , blank=True, null=True)
    user_room_status = models.BooleanField(default=False)
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())


class JoinRoom(models.Model):
    fk_room = models.ForeignKey(Room_Master, on_delete=models.CASCADE , blank=True, null=True  )
    fk_user = models.ForeignKey(UserDetails, on_delete=models.CASCADE , blank=True, null=True  )
    created_dt = models.DateTimeField(blank=True , null= True , default= datetime.datetime.now())
     