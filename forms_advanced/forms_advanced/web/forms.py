from django import forms
from django.forms import modelform_factory

from non_django_demos.callables import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

        # labels = {
        #     "first_name": "First name",
        # }
        #
        # error_messages = {
        #     "first_name": {
        #         "required": "This field is required.",
        #         "unique": "This field is required.",
        #         "max_length": "The name is too long.",
        #     }
        # }


PersonForm2 = modelform_factory(Person, fields='__all__')
