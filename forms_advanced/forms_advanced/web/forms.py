from dataclasses import fields

from django import forms
from django.forms import modelform_factory

from forms_advanced.web.models import Person


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


class BootstrapFormMixin:
    def _init_bootstrap_form(self):
        for _, field in self.fields:
            field.widget.attrs['class'] = 'form-control'


class ReadOnlyFieldsMixin:
    readonly_fields = ()

    def _mark_read_only_fields(self):
        for field_name in self.readonly_fields:
            self.fields[field_name].widget.attrs["readonly"] = "readonly"

        # for _, field in self.fields.items():
        #     field.widget.attrs['readonly'] = 'readonly'


class UpdatePersonForm(ReadOnlyFieldsMixin, PersonForm):
    readonly_fields = ('age', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._mark_read_only_fields()

        self.fields['age'].widget.attrs["readonly"] = "readonly"


PersonForm2 = modelform_factory(Person, fields='__all__')
