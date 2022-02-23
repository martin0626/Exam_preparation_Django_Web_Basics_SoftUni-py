from django.urls import path

from ExamPrep_03.Notes.views import home_view, add_note, edit_note, delete_note, details_note, profile_view, \
    profile_create, delete_profile

urlpatterns = [
    path('', home_view, name='home'),
    path('add/', add_note, name='add note'),
    path('edit/<int:pk>', edit_note, name='edit note'),
    path('delte/<int:pk>', delete_note, name='delete note'),
    path('details/<int:pk>', details_note, name='details note'),
    path('profile/', profile_view, name='profile'),
    path('profile/create', profile_create, name='profile create'),
    path('profile/delete', delete_profile, name='profile delete'),
]
