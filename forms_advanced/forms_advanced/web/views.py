from django.shortcuts import render

from forms_advanced.web.forms import PersonForm, UpdatePersonForm


def index(request):
    person_form = PersonForm()
    update_person_form = UpdatePersonForm()

    context = {
        "person_form": person_form,
        "update_person_form": update_person_form,
    }

    return render(request, "web/index.html", context)