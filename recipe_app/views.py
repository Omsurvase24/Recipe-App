from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def recipe_app(request):
    context = {'page': 'Home'}
    return render(request, "index.html", context)
