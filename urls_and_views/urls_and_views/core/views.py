from django.http import HttpResponse

def index(request, *args, **kwargs):
    return HttpResponse(f"It works with args={args} and kwargs={kwargs}")