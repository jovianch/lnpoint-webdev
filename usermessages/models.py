from django.db import models
from accounts.models import User

class UserMessage(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages')
    receiver = models.ForeignKey(User, related_name='received_messages')
    date_sent = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ['date_sent']
