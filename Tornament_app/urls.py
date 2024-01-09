from  django.urls import path
from .views import *
from .views_aj import *

urlpatterns = [
    path('', index),
    path('createRoom', create_room),
    path('SaveRoom', SaveRoom),
    path('SaveUser', SaveUser),
    path('browesTornaments', browesTornaments),
    path('ViewMore/<int:id>', ViewMore),
    path('joinCustom', joinCustom),
]