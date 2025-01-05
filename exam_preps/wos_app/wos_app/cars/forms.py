from django import forms

from wos_app.cars.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image_url'].widget.attrs['placeholder'] = 'https://...'


class CarCreateForm(CarBaseForm):
    pass
