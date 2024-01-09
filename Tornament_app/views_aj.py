from Project_utilty.decorators import is_authenticated
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def SaveUser(request):
    send_data = {'status': 0, 'msg':'Something went wrong !.'}
    userObj = None
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('pwd')
    if email != None:
        #  User Signup 
        if UserDetails.objects.filter(email = email).exists():
            send_data = {'status': 0 , 'msg' : 'Email Already Exists !'}
        elif UserDetails.objects.filter(username = username).exists():
            send_data = {'status': 0 , 'msg' : 'Username Already Exists !'}
        else:
            userObj = UserDetails.objects.create(username = username, email = email, password = password)
            request.session['user_id'] = str(userObj.id)
            request.session['user_type'] = 'user'
            send_data = {'status': 2, 'msg':"Account has been Created Successfully..."}
    else:
        if  UserDetails.objects.filter(username = username).exists():
            userObj = UserDetails.objects.get(username = username)
            request.session['user_id'] = str(userObj.id)
            request.session['user_type'] = 'user'
            send_data = {'status': 1, 'msg':"Successfully Login to your Account."}
        else:
            send_data = {'status': 0 , 'msg':'Your Account Is Not Found.'}
    return JsonResponse(send_data)



@csrf_exempt
def SaveRoom(request):
    send_data = {'status': 0, 'msg':'Something went wrong.'}
    thumbnail = request.FILES.get('thumbnail')
    title = request.POST.get('title')
    description = request.POST.get('description')
    select_game = request.POST.get('select_game')
    totalMembers = request.POST.get('totalMembers')
    tornamentDt = request.POST.get('tornamentDt')
    StartTm = request.POST.get('StartTm')
    EndTm = request.POST.get('EndTm')
    roomType = request.POST.get('roomType')
    room_pwd = request.POST.get('room_pwd')
    gameType = request.POST.get('gameType')
    select_members = request.POST.get('select_members')
    custom_team = request.POST.get('custom_team')
    map = request.POST.get('map')
    game_room_id = request.POST.get('game_room_id')
    game_room_type = request.POST.get('game_room_type')
    game_room_password = request.POST.get('game_room_password')
    join_status = request.POST.get('join_status')
    joining_fee = request.POST.get('joining_fee')
    userPlayerStatus = False if request.POST.get('userPlayerStatus') == 'false' else True
    user_obj = is_authenticated(request)
    if user_obj:
        creObj = Room_Master.objects.create(fk_user = user_obj, title = title, discription = description, thumbnail = thumbnail, selected_game = select_game , room_member = totalMembers, tornament_dt = tornamentDt, start_tm = StartTm, end_tm = EndTm, room_type = roomType, room_password = room_pwd, game_type = gameType, team_member = select_members, custom_team = custom_team, room_joining = join_status, room_joining_fee = joining_fee , game_map  = map, game_room_id = game_room_id, game_room_type = game_room_type, game_room_type_pwd = game_room_password, user_room_status = userPlayerStatus )
        if userPlayerStatus:
            creObj.available_seats += 1
            JoinRoom.objects.create(fk_room = creObj , fk_user = user_obj)
            creObj.save
        send_data = {'status': 1, 'msg':'Your Room has been successfully created. Lets enjoy .'}
    else:
        send_data = {'status': 0, 'msg':'User Not Login.'}
    return JsonResponse(send_data)


def UpdateRoom(request):
    thumbnail = request.FILES.get('thumbnail')
    title = request.POST.get('title')
    description = request.POST.get('description')
    select_game = request.POST.get('select_game')
    totalMembers = request.POST.get('totalMembers')
    tornamentDt = request.POST.get('tornamentDt')
    StartTm = request.POST.get('StartTm')
    EndTm = request.POST.get('EndTm')
    roomType = request.POST.get('roomType')
    room_pwd = request.POST.get('room_pwd')
    gameType = request.POST.get('gameType')
    select_members = request.POST.get('select_members')
    custom_team = request.POST.get('custom_team')
    map = request.POST.get('map')
    game_room_id = request.POST.get('game_room_id')
    game_room_type = request.POST.get('game_room_type')
    game_room_password = request.POST.get('game_room_password')
    join_status = request.POST.get('join_status')
    joining_fee = request.POST.get('joining_fee')

    data = request.POST.dict()

    user = data['user_id']

    thumbnail = request.FILES.get('thumbnail')
    user_obj = UserDetails.objects.get(id = user)

        
    data.pop('user', None)
    data.pop('thumbnail', None)

    for k, v in data.items():
        setattr(user_obj, k, v)
    

    if thumbnail != None:
        user_obj.thumbnail =  thumbnail

    user_obj.save()
    return JsonResponse({'status':'1','msg':'Profile updated successfully.'})


@csrf_exempt
def joinCustom(request):
    room_id = request.POST.get('room_id')
    user_id = request.POST.get('user_id')
    if Room_Master.objects.filter(id = room_id).exists():
        room_obj = Room_Master.objects.get(id = room_id)
        if Room_Master.room_member == room_obj.available_seats:
            send_data = {'status':0, 'msg':"Seat's not available. Sorry !"}
        else:
            if not JoinRoom.objects.filter(fk_room = room_obj, fk_user__id = user_id).exists():
                room_obj.available_seats += 1
                JoinRoom.objects.create(fk_room = room_obj , fk_user__id = user_id)
                room_obj.save()
                send_data = {'status':1, 'msg':"Notify 10 min before Room Start ."}
            else:
                send_data = {'status':1, 'msg':"You Already Joined this room"}
    else:
        send_data = {'status':0, 'msg':"Something went wrong !"}
    return JsonResponse(send_data)
        