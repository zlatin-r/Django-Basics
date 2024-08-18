from django.http import HttpResponse


def index(request, *args, **kwargs):
    return HttpResponse(f"It works with:<br/>"
               f"args={args} and kwargs={kwargs}<br/>")
               # f"method={request.method}<br/>"
               # f"user={request.user}<br/>"
               # f"path={request.path}<br/>")

