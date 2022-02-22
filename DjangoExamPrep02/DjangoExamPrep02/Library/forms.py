from django import forms

from DjangoExamPrep02.Library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
        })
        self.fields['image_url'].widget.attrs.update({
            'placeholder': 'Image URL',
        })

    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'image_url': 'Image URL',
        }

        widgets = {
            'attrs'
        }


class AddBookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({
            'placeholder': 'Title',
        })

        self.fields['description'].widget.attrs.update({
            'placeholder': 'Description',
            'rows': 3,
        })

        self.fields['image'].widget.attrs.update({
            'placeholder': 'Image',
        })

        self.fields['type'].widget.attrs.update({
            'placeholder': 'Fiction, Novel, Crime..',
        })

    class Meta:
        model = Book
        fields = '__all__'


class EditBookForm(AddBookForm):
    pass


class EditProfileForm(CreateProfileForm):
    pass


class DeleteProfileForm(CreateProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        Book.objects.all().delete()
        self.instance.delete()
        return self.instance

    class Meta:
        model = Profile
        fields = '__all__'




