import datetime

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.shortcuts import render

from chat.models import ConnectedUsers
from channelsWS.cls.state import State

def index(request):
    return render(request, 'chat/index.html')


def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })


def webhook(request):
    channel_layer = get_channel_layer()
    if not channel_layer.groups:
        return HttpResponse('No any groups available')
    async_to_sync(channel_layer.group_send)(
        list(channel_layer.groups.keys())[0],
        {
            'type': 'chat_message',
            'message': 'Hello from the Web. Current time is %s. Time list %s' %
                       (datetime.datetime.now(), State().get_times())
        }
    )
    return HttpResponse("Result is OK. Check the active windows for a new message")


def users_online(request):
    connected_users = [str(user) for user in ConnectedUsers.objects.all()]
    return HttpResponse("Currently connected: %s" % connected_users)
