from django import forms

from fruitipedia_app.fruits.models import Fruit


class FruitCreateForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)

        labels = {
            'name': '',
            'image_url': '',
            'description': '',
            'nutrition': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = "Fruit Name"
        self.fields['image_url'].widget.attrs['placeholder'] = "Fruit Image URL"
        self.fields['description'].widget.attrs['placeholder'] = "Fruit Description"
        self.fields['nutrition'].widget.attrs['placeholder'] = "Nutrition Info"


class FruitEditForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)