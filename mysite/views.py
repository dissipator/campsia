from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')