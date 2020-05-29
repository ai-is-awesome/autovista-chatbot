# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })



def room_admin(request, room_name):
	context = {'room_name' : room_name}
	return render(request, 'chat/admin_room.html')

