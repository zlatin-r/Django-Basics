from django import forms

from fruitipedia_app.fruits.models import Fruit


class FruitBaseForm(forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ('owner',)


class FruitCreateForm(FruitBaseForm):
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


class FruitEditForm(FruitBaseForm):
    pass

class FruitDeleteForm(FruitBaseForm):
    class Meta:
        model = Fruit
        exclude = ('owner', 'nutrition')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
