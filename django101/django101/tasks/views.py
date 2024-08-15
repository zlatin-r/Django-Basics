from django.shortcuts import render
from django.http import HttpResponse

from django101.tasks.models import Task


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    output = "; ".join(f"{t.title}: {t.description}" for t in tasks)

    if not output:
        output = "No tasks"

    return HttpResponse(output)