from django.urls import path

from WebBasicsExam.web.views import home_page, add_album, details_album, edit_album, delete_album, profile_details, \
    profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('album/add/', add_album, name='add album page'),
    path('album/details/<int:pk>', details_album, name='album details page'),
    path('album/edit/<int:pk>', edit_album, name='edit album page'),
    path('album/delete/<int:pk>', delete_album, name='delete album page'),
    path('profile/details/', profile_details, name='profile details page'),
    path('profile/delete/', profile_delete, name='delete profile page'),
]


# •	http://localhost:8000/ - home page
# •	http://localhost:8000/album/add/ - add album page
# •	http://localhost:8000/album/details/<id>/ - album details page
# •	http://localhost:8000/album/edit/<id>/ - edit album page
# •	http://localhost:8000/album/delete/<id>/ - delete album page
# •	http://localhost:8000/profile/details/ - profile details page
# •	http://localhost:8000/profile/delete/ - delete profile page