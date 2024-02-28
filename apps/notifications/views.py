from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, "notifications/index.html")


def test(request):
    channel_layer = get_channel_layer()
    user = request.user
    async_to_sync(channel_layer.group_send)(
        f"notification_{user.username}",  # Group name
        {
            "type": "notification_message",
            "message": f"This is a message from {user.username}",
            "user": user.username,
        },
    )
    return HttpResponse("Sent")
