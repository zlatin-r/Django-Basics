from django import forms

from wos_app.user_profile.models import UserProfile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput,
        }
