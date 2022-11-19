from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def healthCheck(request):
    return render(request, 'avanzo/health.html')


def index(request):
    return render(request, 'avanzo/index.html')
