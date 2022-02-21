from django.shortcuts import render, redirect

from DjangoExamPrep01.Expenses.form_actions import FormAction
from DjangoExamPrep01.Expenses.forms import ProfileCreateForm, CreateExpenseForm, EditExpenseForm, DeleteExpenseForm, \
    DeleteProfileForm, EditProfileForm
from DjangoExamPrep01.Expenses.models import Profile, Expense


def get_profile():
    profile =Profile.objects.first()
    return profile


def budget_left():
    profile = get_profile()
    expenses = sum([exp.price for exp in Expense.objects.all()])
    return profile.budget - expenses


def create_profile(request):
    context = {
        'is_not_profile': True,
    }
    form = ProfileCreateForm
    return FormAction.form_without_instance(request, 'home-no-profile.html', context, 'home', form, True)


def home_view(request):
    if get_profile():
        profile = get_profile()
        expenses = Expense.objects.all()
        context = {
            'expenses': expenses,
            'profile': profile,
            'budget_left': budget_left(),
        }
        return render(request, 'home-with-profile.html', context)

    else:
        return create_profile(request)


def create_expense_view(request):
    template = 'expense-create.html'
    context = {}
    redirect_to = 'home'
    form = CreateExpenseForm
    return FormAction.form_without_instance(request, template, context, redirect_to, form)


def edit_expense_edit(request, pk):
    template = 'expense-edit.html'
    redirect_to = 'home'
    form = EditExpenseForm
    instance = Expense.objects.get(pk=pk)
    context = {
        'expense': instance
    }
    return FormAction.form_with_instance(request, template, context, redirect_to, form, instance)


def delete_expense_view(request, pk):
    template = 'expense-delete.html'
    redirect_to = 'home'
    form = DeleteExpenseForm
    instance = Expense.objects.get(pk=pk)
    context = {
        'expense': instance,
    }
    return FormAction.form_with_instance(request, template, context, redirect_to, form, instance)


def profile_view(request):
    profile = get_profile()

    expenses_count = Expense.objects.count()

    context = {
        'profile': profile,
        'expenses_count': expenses_count,
        'budget_left': budget_left(),
    }

    return render(request, 'profile.html', context)


def profile_edit_view(request):
    template = 'profile-edit.html'
    redirect_to = 'profile'
    form = EditProfileForm
    instance = get_profile()
    context = {
        'expense': instance,
    }
    return FormAction.form_with_instance(request, template, context, redirect_to, form, instance, True)


def profile_delete_view(request):
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=get_profile())
        if form.is_valid():
            form.save()
            return redirect('profile create')

    return render(request, 'profile-delete.html')
