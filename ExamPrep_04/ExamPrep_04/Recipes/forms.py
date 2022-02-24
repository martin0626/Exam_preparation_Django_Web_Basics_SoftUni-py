from django import forms

from ExamPrep_04.Recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

        labels = {
            'image_url': 'Image URL',
            'time': 'Time (Minutes)'
        }


class EditRecipeForm(CreateRecipeForm):
    pass


class DeleteRecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.required = False

    class Meta:
        model = Recipe
        fields = '__all__'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
