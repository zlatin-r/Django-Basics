from django import forms

from traveler.models import Traveler


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Traveler
        exclude = ("about_me",)

        error_massages = {
            "nickname": {
                "max_length": "Your nickname is invalid!",
            }
        }

        help_texts = {
            "nickname": "*Nicknames can contain only letters and digits."
        }


class CreateProfileForm(ProfileBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["nickname"].widget.attrs["placeholder"] = "Enter a unique nickname..."
        self.fields["email"].widget.attrs["placeholder"] = "Enter a valid email address..."
        self.fields["country"].widget.attrs["placeholder"] = "Enter a country code like <BGR>..."


class EditProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ()


class DeleteProfileForm(ProfileBaseForm):
    class Meta:
        exclude = ()
