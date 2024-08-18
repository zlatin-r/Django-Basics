import time

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse(f"Response from {time.time()}")

