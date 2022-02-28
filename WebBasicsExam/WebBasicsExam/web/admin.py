from django.contrib import admin

from WebBasicsExam.web.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(Album)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name']
