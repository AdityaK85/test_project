from django.shortcuts import render
from django.views.decorators.cache import cache_control
from Project_utilty.decorators import *
from .models import *
from datetime import datetime , timedelta , date , timezone

today = datetime.today()

# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    user_obj = is_authenticated(request)
    context ={
        'user_obj':user_obj,
    }
    return render(request, 'index.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def create_room(request):
    user_obj = is_authenticated(request)
    context ={
        'user_obj':user_obj,
    }
    return render(request, 'createRoom.html', context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def browesTornaments(request):
    global today
    user_obj = is_authenticated(request)
    tornaments_obj = Room_Master.objects.all().order_by('-id')
    for i in tornaments_obj:
        if i.tornament_dt < today.replace(tzinfo=timezone.utc):
            i.room_status = 'Closed'
        elif i.tornament_dt >= today.replace(tzinfo=timezone.utc):
            i.room_status = 'Open'
        else:
            i.room_status = "Upcomming"
    context ={
        'user_obj':user_obj,
        'tornaments_obj':tornaments_obj,
    }
    return render(request, 'browse.html', context)


def room_availability(input_date, input_time):
    # Convert input date and time to datetime object
    input_datetime = datetime.combine(input_date, input_time)

    # Get current date and time
    current_datetime = datetime.now()

    # Get the current date only (without time)
    current_date = current_datetime.date()

    # Ensure input_date is a datetime.date object
    if isinstance(input_date, datetime):
        input_date = input_date.date()

    # Check if the input date is today
    if input_date == current_date:
        # Check if the input time is the current time
        if input_time.hour == current_datetime.hour and input_time.minute == current_datetime.minute:
            return "Live"
        else:
            return "Today"
        
    # Check if the input date is in the past
    elif input_date  <= current_date:
        return "Closed"
    
    # Check if the input date is tomorrow
    elif input_date == current_date + timedelta(days=1):
        return "Tomorrow"
    
    else:
        return 'Upcoming'
    


def ViewMore(request, id):
    user_obj = is_authenticated(request)
    tornament_obj = Room_Master.objects.get(id = id) if Room_Master.objects.filter(id = id).exists() else None
    date_tm = room_availability(tornament_obj.tornament_dt , tornament_obj.start_tm)
    context ={
        'user_obj':user_obj,
        'tornaments_obj':tornament_obj,
        'date_tm':date_tm,
    }
    return render(request, 'ViewTornaments.html', context)
