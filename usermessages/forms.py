from django import forms

from .models import UserMessage


class ChatUserMessage(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control form-chat','placeholder':'Enter messages here...'}))

    class Meta:
        model = UserMessage
        fields = (
            'message',
        )









