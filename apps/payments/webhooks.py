import stripe
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from apps.orders.models import Order

channel_layer = get_channel_layer()


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.headers.get("Stripe-Signature")
    event = None
    try:
        event = stripe.Webhook.construct_event(payload, sig_header, settings.STRIPE_WEBHOOK_SECRET)
    except ValueError:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        # Invalid signature
        return HttpResponse(status=400)
    if event.type == "checkout.session.completed":
        session = event.data.object
        if session.mode == "payment" and session.payment_status == "paid":
            try:
                order = Order.objects.get(id=session.client_reference_id)
            except Order.DoesNotExist:
                return HttpResponse(status=404)
        # mark order as paid
        order.paid = True
        order.status = Order.OrderStatus.PAID
        # store Stripe payment ID
        order.stripe_id = session.payment_intent
        order.save()
        # Send Notification to the user
        async_to_sync(channel_layer.group_send)(
            f"notification_{order.user.username}",
            {
                "type": "notification_message",
                "message": f"Order {order.id} has been paid",
                "user": order.user.username,
            },
        )
    return HttpResponse(status=200)
