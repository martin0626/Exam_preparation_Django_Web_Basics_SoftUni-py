from django import forms

from WebBasicsExam.web.models import Profile, Album


class CreateUserForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': 'Username',
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Email',
        })
        self.fields['age'].widget.attrs.update({
            'placeholder': 'Age',
        })

    class Meta:
        model = Profile
        fields = '__all__'
        labels = {
            'username': 'Username',
            'email': 'Email',
            'age': 'Age',
        }


class AddAlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Album Name',
        })
        self.fields['artist'].widget.attrs.update({
            'placeholder': 'Artist',
        })
        self.fields['description'].widget.attrs.update({
            'placeholder': 'Description',
        })
        self.fields['image_url'].widget.attrs.update({
            'placeholder': 'Image URL',
        })
        self.fields['price'].widget.attrs.update({
            'placeholder': 'Price',
        })

    class Meta:
        model = Album
        fields = '__all__'

        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }


class EditAlbumForm(AddAlbumForm):
    pass


class DeleteAlbumForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
        labels = {
            'name': 'Album Name',
            'image_url': 'Image URL',
        }


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ()

    def save(self, commit=True):
        Album.objects.all().delete()
        self.instance.delete()
        return self.instance


