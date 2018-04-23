from django.contrib import admin

from .models import UserMessage

class UserMessageAdmin(admin.ModelAdmin):
    list_display = ['message','sender','receiver','date_sent']
    search_fields = ['message', 'sender', 'receiver']
    list_per_page = 50

admin.site.register(UserMessage, UserMessageAdmin)

# Register your models here.