#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
