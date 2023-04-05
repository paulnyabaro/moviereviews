from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': searchTerm})

def about(request):
    return HttpResponse('<h1>This is the about page</h1>')