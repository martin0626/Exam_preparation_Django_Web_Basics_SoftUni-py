from django.shortcuts import render, redirect

from ExamPrep_03.Notes.forms import CreateProfileForm, CreateNoteForm, DeleteNoteForm, EditNoteForm, DeleteProfileForm
from ExamPrep_03.Notes.helpers import get_profile
from ExamPrep_03.Notes.models import Note


def home_view(request):
    profile = get_profile()
    if not profile:
        return profile_create(request)

    notes = Note.objects.all()
    context = {
        'notes': notes,
    }

    return render(request, 'home-with-profile.html', context)


def add_note(request):
    if request.method == 'POST':
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateNoteForm()

    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def edit_note(request, pk):
    note = Note.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EditNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = DeleteNoteForm(instance=note)

    context = {
        'form': form,
        'note': note,
    }

    return render(request, 'note-delete.html', context)


def details_note(request, pk):
    note = Note.objects.get(pk=pk)

    context = {
        'note': note,
    }

    return render(request, 'note-details.html', context)


def profile_view(request):
    notes_count = Note.objects.count()
    context = {
        'notes_count': notes_count,
    }
    return render(request, 'profile.html', context)


def profile_create(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfileForm()

    context = {
        'form': form
    }
    return render(request, 'home-no-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    notes = Note.objects.all()

    notes.delete()
    profile.delete()
    return redirect('profile create')