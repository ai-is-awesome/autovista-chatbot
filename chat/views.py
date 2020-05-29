# chat/views.py
from django.shortcuts import render
from django.urls import reverse


def index(request):
	context = {'url' : reverse(index)}
	return render(request, 'chat/index.html', context)




def room(request, room_name):
	url = '/chat/%s/admin' % (room_name)
	if url == reverse(room, kwargs = {'room_name' : room_name}):
		admin = True

	else:
		admin = False
	print('Admin is: ', admin)
	return render(request, 'chat/room.html', {
		'room_name': room_name, 
		'admin' : admin, 
    })



def room_admin(request, room_name):
	context = {'room_name' : room_name}

	return render(request, 'chat/admin_room.html')





