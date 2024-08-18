from django.http import HttpResponse, JsonResponse


def index(request, *args, **kwargs):
    content = (f"It works with:<br/>"
               f"args={args} and kwargs={kwargs}<br/>"
               f"method={request.method}<br/>"
               f"user={request.user}<br/>"
               f"path={request.path}<br/>")

    return HttpResponse(
        content,
        content_type="application/json"
    )

def index_json(request, *args, **kwargs):
    content = {
        "args": args,
        "kwargs": kwargs,
        "path": request.path,
        "method": request.method,
        "user": str(request.user),
    }

    return JsonResponse(
        content,
        content_type="application/json",
        # status=201,
    )
