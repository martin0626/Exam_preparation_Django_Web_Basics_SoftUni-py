from django.shortcuts import render, redirect

from DjangoExamPrep02.Library.forms import CreateProfileForm, AddBookForm, EditBookForm, EditProfileForm, \
    DeleteProfileForm
from DjangoExamPrep02.Library.helpers import get_profile
from DjangoExamPrep02.Library.models import Book


def home_view(request):
    profile = get_profile()
    if profile:
        books = Book.objects.all()

        context = {
            'books': books,
        }

        return render(request, 'home-with-profile.html', context)

    return create_profile(request)


def add_book(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddBookForm()

    context = {
        'form': form,
    }

    return render(request, 'add-book.html', context)


def edit_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = EditBookForm(instance=book)
    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'edit-book.html', context)


def details_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }

    return render(request, 'book-details.html', context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return redirect('home')


def profile_view(request):
    profile = get_profile()

    return render(request, 'profile.html')


def edit_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view profile')

    else:
        form = EditProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()

    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'home-no-profile.html', context)
