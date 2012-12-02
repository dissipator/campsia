from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from users.models import User

def index(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'users/index.html', context)