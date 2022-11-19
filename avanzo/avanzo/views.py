from django import http   
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def healthCheck(request):
    r1 = http.request('GET', 'http://34.70.63.249:8080')
    r2 = http.request('GET', 'http://35.232.6.147:8080')
    return HttpResponse(r1+r2)

def index(request):
    return render(request, 'avanzo/index.html')