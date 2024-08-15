import http

from django.shortcuts import render
from django.http import HttpResponse
from django.template.defaultfilters import title

from django101.tasks.models import Task


# Create your views here.

# def index(request):
#     title_filter = request.GET.get('filter', '')
#
#     tasks = Task.objects.all()
#
#     if title_filter:
#         tasks = tasks.filter(title__icontains=title_filter.lower())
#
#     result = []
#
#     if not tasks:
#         return HttpResponse("<h1>No tasks !!!</h1>")
#     else:
#         for task in tasks:
#             result.append(f"""
#             <li>
#                 <h2>{task.title}</h2>
#                 <p>{task.description}</p>
#             </li>""")
#
#     ul = f"<ul>{''.join(result)}</ul>"
#
#     content = f"""
#         <h1>{len(tasks)} Tasks</h1>
#         {ul}"""
#
#     return HttpResponse(content)

def index(request):
    title_filter = request.GET.get('filter', None)

    tasks = Task.objects.all()

    if title_filter:
        tasks = tasks.filter(title__icontains=title_filter.lower())

    context = {
        "title": "The tasks app!!!",
        "task_list": tasks,
        "tasks_count": tasks.count(),
    }

    return render(request, 'tasks/index.html', context)