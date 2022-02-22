from django.urls import path

from DjangoExamPrep02.Library.views import home_view, add_book, edit_book, details_book, profile_view, edit_profile, \
    delete_profile, create_profile, delete_book

urlpatterns = [
    path('', home_view, name='home'),
    path('add/', add_book, name='add book'),
    path('edit/<int:pk>/', edit_book, name='edit book'),
    path('details/<int:pk>/', details_book, name='details book'),
    path('delete/<int:pk>/', delete_book, name='delete book'),
    path('profile/', profile_view, name='view profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
    path('create/profile/', create_profile, name='create profile')
]

# •	http://localhost:8000/ - home page
# •	http://localhost:8000/add/ - add book page
# •	http://localhost:8000/edit/:id - edit book page
# •	http://localhost:8000/details/:id - book details page

# •	http://localhost:8000/profile/ - profile page
# •	http://localhost:8000/profile/edit/ - edit profile page
# •	http://localhost:8000/profile/delete/ - delete profile page