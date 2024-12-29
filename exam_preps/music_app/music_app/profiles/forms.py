from django import forms

from music_app.mixins import PlaceholderMixin
from music_app.profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    pass
