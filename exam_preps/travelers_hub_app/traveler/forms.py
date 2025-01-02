from django import forms

from traveler.models import Traveler


class TravelerBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ('traveler',)


class TravelerCreateForm(TravelerBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nickname'].widget.attrs['placeholder'] = 'Enter a unique nickname...'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter a valid email address...'
        self.fields['country'].widget.attrs['placeholder'] = 'Enter a country code like <BGR>...'


class TravelerDetailsForm(TravelerBaseForm):
    pass


class TravelerEditForm(TravelerBaseForm):
    pass
