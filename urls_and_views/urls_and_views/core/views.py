from django.http import HttpResponse
from django.shortcuts import render

def index(request, *args, **kwargs):
    return HttpResponse(f"It works with args={args} and kwargs={kwargs}")