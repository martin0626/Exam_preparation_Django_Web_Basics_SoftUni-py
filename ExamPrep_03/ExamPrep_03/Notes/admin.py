from django.contrib import admin

# Register your models here.
from ExamPrep_03.Notes.models import Profile, Note


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name']


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']
