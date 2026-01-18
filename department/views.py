from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

def index_department(request,id):
    return HttpResponse(f'Hello {id}, welcome to the Department index page.', content_type='text/plain')

def slug_view(request,slug):
    return HttpResponse(f'{slug} you are slug, welcome to the Department index page.', content_type='text/plain')

