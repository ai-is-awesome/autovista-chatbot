# chat/views.py
from django.shortcuts import render
from django.urls import reverse


def index(request):
	context = {'url' : reverse(index)}
	return render(request, 'chat/index.html', context)




def room(request, room_name):
	url = '/chat/%s/admin' % (room_name)
	current_url = reverse(room, kwargs = {'room_name' : room_name})

	user_url = 'http://localhost:8000/chat/%s/' %  (room_name)
	current_url = request.build_absolute_uri()


	print('URL is :', current_url)
	print('user_url is : %s' % (user_url))
	if user_url == current_url:
		admin = True
		print('URL is : %s' % (reverse(room, kwargs = {'room_name' : room_name})))
		return render(request, 'chat/room.html', {'room_name' : room_name, 'admin' : admin})



	if url == reverse(room, kwargs = {'room_name' : room_name}) and request.user.is_superuser:
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





