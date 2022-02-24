from django.contrib import admin

from ExamPrep_04.Recipes.models import Recipe


@admin.register(Recipe)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['title']
