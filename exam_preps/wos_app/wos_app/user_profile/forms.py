from django import forms

from wos_app.user_profile.models import UserProfile


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput,
        }


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.fields['age'].help_text = ""


class ProfileDeleteForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ()
