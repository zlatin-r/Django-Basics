from events.models import Events
from django import forms


class EventBaseForm(forms.ModelForm):
    class Meta:
        model = Events
        exclude = ["organizer"]

        labels = {
            "start_time": "Event Date/Time:",
            "key_features": "Event Key Features:",
            "available_tickets": "Available Tickets:",
            "banner_url": "Event Banner URL:",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["slogan"].widget.attrs["placeholder"] = "Provide an appealing text..."
        self.fields['key_features'].widget.attrs['placeholder'] = "Provide important event details..."
        self.fields['banner_url'].widget.attrs['placeholder'] = "An optional banner image URL..."
        self.fields["start_time"].widget = forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control datetimepicker-input",
                "data-target": "#datetimepicker1"
            }
        )


class EventCreateForm(EventBaseForm):
    pass


class EditEventForm(EventCreateForm):
    pass


class DeleteEventForm(EventBaseForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.disabled = True
