from django.shortcuts import render

# Create your views here.
from django. http import HttpResponse
def homePage(request):
    return HttpResponse("<h1>Hello Turyakira_Technologies</h1>")