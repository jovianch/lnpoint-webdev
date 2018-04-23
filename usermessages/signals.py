from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from usermessages.models import UserMessage
from clients.twilio_api import TwilioAPI


@receiver(post_save, sender=UserMessage)
def notify_user(sender, instance, **kwargs):
    message_receiver = instance.receiver

    if message_receiver.should_notify_new_message():
        api = TwilioAPI()
        message = api.notify_user_new_message(message_receiver)
        message_receiver.last_notified_message = timezone.now()
        message_receiver.save()
