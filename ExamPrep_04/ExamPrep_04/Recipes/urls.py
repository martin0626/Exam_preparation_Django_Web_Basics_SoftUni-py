from django.urls import path

from ExamPrep_04.Recipes.views import home_view, create_recipe, edit_recipe, details_view, delete_recipe

urlpatterns = [
    path('', home_view, name='home'),
    path('create', create_recipe, name='create recipe'),
    path('edit/<int:pk>', edit_recipe, name='edit recipe'),
    path('delete/<int:pk>', delete_recipe, name='delete recipe'),
    path('details/<int:pk>', details_view, name='details'),
]
