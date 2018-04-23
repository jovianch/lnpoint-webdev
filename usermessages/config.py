from django.apps import AppConfig


class UserMessagesConfig(AppConfig):
    name = 'usermessages'

    def ready(self):
        import usermessages.signals
