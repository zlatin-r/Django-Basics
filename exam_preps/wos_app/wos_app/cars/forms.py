from django import forms

from wos_app.cars.models import Car


class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)