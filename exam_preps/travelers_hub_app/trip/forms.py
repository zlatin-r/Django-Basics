from django import forms

from trip.models import Trip


class TripBaseForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'


class CreateTripForm(TripBaseForm):
    labels = {
        'start_date': 'Started on',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['destination'].widget.attrs['placeholder'] = "Enter a short destination note..."
        self.fields['summary'].widget.attrs['placeholder'] = "Share your exciting moments..."
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['duration'].widget.attrs['placeholder'] = "*Duration in days is expected."
        self.fields['image_url'].widget.atrs['placeholder'] = "An optional image URL..."
