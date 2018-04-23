from django.conf import settings
from twilio.rest import Client

class TwilioAPI:
    def __init__(self,
                 account_sid=settings.TWILIO_ACCOUNT_SID,
                 auth_token=settings.TWILIO_AUTH_TOKEN):
        self.client = Client(account_sid, auth_token)

    def send_message(self, to, message, from_=settings.TWILIO_FROM):
        message = self.client.messages.create(
            to=to,
            from_=from_,
            body=str(message)
        )

        return message

    def notify_user_new_message(self, user, from_=settings.TWILIO_FROM):
        phone_number = user.get_phone_number()

        message = ("Hai {user_fullname}\n\n"
                   "Kamu mendapat pesan baru di lnpoint.\n"
                   "Kunjungi lnpoint.com/messages/ untuk melihat pesan tersebut.\n\n"
                   "Thank you, happy sharing!").format(user_fullname=user.fullname)

        return self.send_message(phone_number, message, from_)
