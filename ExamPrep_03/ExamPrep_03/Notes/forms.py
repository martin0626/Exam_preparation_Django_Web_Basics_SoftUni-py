from django import forms

from ExamPrep_03.Notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'First Name',
        })
        self.fields['last_name'].widget.attrs.update({
            'placeholder': 'Last Name',
        })
        self.fields['age'].widget.attrs.update({
            'placeholder': 'Age',
        })
        self.fields['image_url'].widget.attrs.update({
            'placeholder': 'Link to Profile Image',
        })

    class Meta:
        model = Profile
        fields = '__all__'

        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'age': 'Age',
            'image_url': 'Link to Profile Image',
        }


class CreateNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content'].widget.attrs.update({
            'rows': 5,
        })

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']

        labels = {
            'image_url': 'Link to Image'
        }


class EditNoteForm(CreateNoteForm):
    pass


class DeleteNoteForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Note
        fields = ['title', 'content', 'image_url']


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        self.instance.delete()
        Note.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()
