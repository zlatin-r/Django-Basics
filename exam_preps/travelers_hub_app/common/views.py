from http.client import HTTPResponse

from django.shortcuts import render

def show_home_page(request):
    return render(request, template_name='index.html')