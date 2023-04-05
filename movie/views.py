from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Welcome to the homepage</h1>')

def about(request):
    return HttpResponse('<h1>This is the about page</h1>')