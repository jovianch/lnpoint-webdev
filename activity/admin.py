from django.contrib import admin

from .models import Activity, Tag, UserJoinActivity

class UserJoinActivityInLine(admin.TabularInline):
    model = UserJoinActivity

class ActivityAdmin(admin.ModelAdmin):
    model = Activity
    exclude = ('tags',)
    inlines = (UserJoinActivityInLine,)

admin.site.register(Activity, ActivityAdmin)