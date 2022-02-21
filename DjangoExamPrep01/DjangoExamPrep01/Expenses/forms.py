import os

from django import forms

from DjangoExamPrep01.Expenses.models import Profile, Expense


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['budget', 'first_name', 'last_name', 'image']

        labels = {
            'budget': 'Budget',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image': 'Profile Image',
        }


class CreateExpenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = ['title', 'description', 'image', 'price']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }


class EditExpenseForm(CreateExpenseForm):
    pass


class DeleteExpenseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
            self.instance.delete()
            return self.instance

    class Meta:
        model = Expense
        fields = ['title', 'description', 'image', 'price']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'Link to Image',
            'price': 'Price',
        }


class EditProfileForm(ProfileCreateForm):
    pass


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        image_path = None
        if self.instance.image:
            image_path = self.instance.image.path
        self.instance.delete()
        Expense.objects.all().delete()
        if image_path:
            os.remove(image_path)
        return self.instance

    class Meta:
        model = Expense
        fields = ()
