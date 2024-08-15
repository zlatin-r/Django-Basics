import http

from django.shortcuts import render
from django.http import HttpResponse

from django101.tasks.models import Task


# Create your views here.

def index(request):
    tasks = Task.objects.all()

    result = []

    if not tasks:
        return HttpResponse("<h1>No tasks !!!</h1>")
    else:
        for task in tasks:
            result.append(f"""
            <li> 
                <h2>{task.title}</h2>
                <p>{task.description}</p>
            </li>""")

    ul = f"<ul>{''.join(result)}</ul>"

    content = f"""
        <h1>{len(tasks)} Tasks</h1>
        {ul}"""

    return HttpResponse(content)
