from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from users.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'users/index.html', context)


@login_required
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'users/detail.html',{'users':user})
