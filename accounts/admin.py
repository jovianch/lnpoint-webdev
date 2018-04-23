from django.contrib import admin
from profiles.models import Profile
from .models import User
#from profiles.models import Skill





class ProfileInLine(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileInLine,]
    list_display = ['username', 'fullname', 'date_joined', 'card_id', 'contact','phone_number','is_verified']
    search_fields = ['username', 'fullname', 'card_id', 'contact']
    list_per_page = 25

admin.site.register(User,UserAdmin)