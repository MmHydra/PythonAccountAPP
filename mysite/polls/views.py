#from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world")

def pic(request):
    return HttpResponse("i am a dragon")
