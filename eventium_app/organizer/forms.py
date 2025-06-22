from django import forms
from .models import Organizer


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Organizer
        exclude = ["organizer"]

        error_messages = {
            'phone_number': {
                'unique': "That phone number is already in use!",
            },
        }

        widgets = {
            "secret_key": forms.PasswordInput(),
        }

        labels = {
            "company_name": "Company Name:",
            "phone_number": "Phone Number:",
            "secret_key": "Secret Key:"
        }


class ProfileCreateForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        exclude = ["website", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["company_name"].widget.attrs["placeholder"] = "Enter a company name..."
        self.fields["phone_number"].widget.attrs["placeholder"] = "Enter a valid phone number (digits only)..."
        self.fields["secret_key"].widget.attrs["placeholder"] = "Enter a secret key like <1234>..."


class EditProfileForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):
        fields = ["company_name", "phone_number", "website"]
