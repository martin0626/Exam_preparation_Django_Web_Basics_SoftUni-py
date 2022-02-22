from django.contrib import admin

from DjangoExamPrep02.Library.models import Book, Profile


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name']
