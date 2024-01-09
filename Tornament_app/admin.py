from django.contrib import admin
from .models import *
# Register your models here.


class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'password')
admin.site.register(UserDetails, UserDetailsAdmin)

class JoinRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'fk_room', 'fk_user', 'created_dt')
admin.site.register(JoinRoom, JoinRoomAdmin)


class Room_MasterAdmin(admin.ModelAdmin):
    list_display = ('id','fk_user' , 'title','selected_game', 'room_member','tornament_dt','start_tm','end_tm','room_type','room_password', 'game_type', 'team_member', 'custom_team', 'room_joining', 'room_joining_fee', 'game_map', 'game_room_id', 'game_room_type_pwd', 'available_seats')
    list_filter = ('fk_user', )
admin.site.register(Room_Master, Room_MasterAdmin)