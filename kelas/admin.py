from django.contrib import admin

from .models import OpenClass, Tag, Category

class OpenClassAdmin(admin.ModelAdmin):
    model = OpenClass
    filter_horizontal = ('categories',)

admin.site.register(OpenClass, OpenClassAdmin)
admin.site.register(Category)


# Register your models here.
