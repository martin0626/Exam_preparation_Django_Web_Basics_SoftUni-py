from django.urls import path

from DjangoExamPrep01.Expenses.views import create_expense_view, home_view, edit_expense_edit, delete_expense_view, \
    profile_view, profile_edit_view, profile_delete_view, create_profile

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_expense_view, name='create expense'),
    path('edit/<int:pk>', edit_expense_edit, name='edit expense'),
    path('delete/<int:pk>', delete_expense_view, name='delete expense'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit', profile_edit_view, name='profile edit'),
    path('profile/delete', profile_delete_view, name='profile delete'),
    path('profile/create', create_profile, name='profile create'),
]
