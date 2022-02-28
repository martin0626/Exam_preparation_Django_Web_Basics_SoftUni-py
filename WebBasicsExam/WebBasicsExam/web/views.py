from django.shortcuts import render, redirect

from WebBasicsExam.web.forms import CreateUserForm, AddAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from WebBasicsExam.web.models import Profile, Album


def get_profile():
    profile = Profile.objects.first()
    return profile


def home_page(request):
    profile = get_profile()
    albums = Album.objects.all()

    if profile:
        context = {
            'albums': albums
        }
        return render(request, 'home-with-profile.html', context)

    return profile_create(request)


def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = AddAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def details_album(request, pk):
    album = Album.objects.get(pk=pk)

    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def edit_album(request, pk):
    album = Album.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditAlbumForm(instance=album)

    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def delete_album(request, pk):
    album = Album.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    else:
        form = DeleteAlbumForm(instance=album)

    context = {
        'form': form,
        'album': album,

    }
    return render(request, 'delete-album.html', context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'albums_count': albums_count,
    }
    return render(request, 'profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    context = {

    }
    return render(request, 'profile-delete.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = CreateUserForm()
    context = {
        'form': form,
        'no_profile': True,
    }
    return render(request, 'home-no-profile.html', context)
